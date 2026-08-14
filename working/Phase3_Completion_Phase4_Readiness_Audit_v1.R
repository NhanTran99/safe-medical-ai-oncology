# ============================================================
# PHASE 3 COMPLETION & PHASE 4 READINESS AUDIT v1
# ============================================================
# READ-ONLY audit.
#
# Purpose:
#   Final reconciliation of:
#     239 Population Packages
#     4 Gold artifacts per PP
#     Population Package Integration Manifest
#     Git repository state / immutable commit
#
# This script does NOT modify artifacts, manifest, or Git.
#
# IMPORTANT:
#   Manifest column names may differ between project revisions.
#   The script first detects likely columns and reports what it used.
#   It does not silently rewrite the manifest.
# ============================================================

options(stringsAsFactors = FALSE, warn = 1)

REPO_ROOT <- normalizePath(
  "D:/GIT hub/safe-medical-ai-oncology",
  winslash = "/", mustWork = TRUE
)

PP_ROOT <- file.path(
  REPO_ROOT, "03_Clinical_Knowledge", "population", "population_packages"
)

WORK_ROOT <- file.path(
  REPO_ROOT, "working"
)

AUDIT_ROOT <- file.path(
  WORK_ROOT, "Phase3_Completion_Phase4_Readiness_Audit"
)

# ---- CONFIG: edit only if your manifest filename/path differs ----

manifest_candidates <- c(
  file.path(REPO_ROOT, "03_Clinical_Knowledge/population/POPULATION PACKAGE INTEGRATION MANIFEST.xlsx"),
  file.path(REPO_ROOT, "03_Clinical_Knowledge/population/Population Package Integration Manifest.xlsx"),
  file.path(REPO_ROOT, "03_Clinical_Knowledge/population/POPULATION_PACKAGE_INTEGRATION_MANIFEST.xlsx"),
  file.path(REPO_ROOT, "working/POPULATION PACKAGE INTEGRATION MANIFEST.xlsx"),
  file.path(REPO_ROOT, "working/Layer4_Integration/POPULATION PACKAGE INTEGRATION MANIFEST.xlsx")
)

if (!dir.exists(AUDIT_ROOT)) {
  dir.create(AUDIT_ROOT, recursive = TRUE, showWarnings = FALSE)
}

EXPECTED_PP_IDS <- sprintf("PP-%04d", 1:239)

EXPECTED_FILES <- c(
  "01_CKO.md",
  "02_KNOWLEDGE_PASSPORT.md",
  "03_PRIMARY_EVIDENCE_PACKAGE.md",
  "04_QA_REPORT.md"
)

EXPECTED_COMMIT <- "ff30308b9e8ccac17e6a52f04daa162923f75889"
EXPECTED_REMOTE <- "https://github.com/NhanTran99/safe-medical-ai-oncology.git"

# ---- helpers ----

read_text <- function(path) {
  if (!file.exists(path)) return("")
  x <- tryCatch(
    readLines(path, encoding = "UTF-8", warn = FALSE),
    error = function(e) character()
  )
  paste(x, collapse = "\n")
}

normalize <- function(x) {
  x <- ifelse(is.na(x), "", as.character(x))
  x <- gsub("[\u2012\u2013\u2014]", "-", x)
  x <- gsub("[[:space:]]+", " ", trimws(x))
  tolower(x)
}

extract_pp <- function(x) {
  if (is.na(x) || !nzchar(as.character(x))) return(character())
  m <- gregexpr("PP-[0-9]{4}", as.character(x), perl = TRUE)[[1]]
  if (length(m) == 1L && m[1] == -1L) return(character())
  unique(regmatches(as.character(x), list(m))[[1]])
}

folder_id <- function(path) {
  b <- basename(path)
  m <- regexec("^(PP-[0-9]{4})(?:\\s|$|[^0-9])", b, perl = TRUE)
  z <- regmatches(b, m)[[1]]
  if (length(z) >= 2L) z[2] else NA_character_
}

find_column <- function(nms, patterns) {
  z <- normalize(nms)
  for (p in patterns) {
    hit <- which(grepl(p, z, perl = TRUE))
    if (length(hit)) return(nms[hit[1]])
  }
  NA_character_
}

safe_csv <- function(df, file) {
  write.csv(df, file, row.names = FALSE, fileEncoding = "UTF-8")
}

# ============================================================
# 1. REPOSITORY / FOLDER AUDIT
# ============================================================

if (!dir.exists(PP_ROOT)) {
  stop(paste("Population Package root not found:", PP_ROOT))
}

pp_dirs <- list.dirs(PP_ROOT, recursive = FALSE, full.names = TRUE)
pp_ids <- vapply(pp_dirs, folder_id, character(1))

folder_rows <- lapply(EXPECTED_PP_IDS, function(id) {

  idx <- which(pp_ids == id)

  if (!length(idx)) {
    return(data.frame(
      PP_ID = id,
      Folder_Found = FALSE,
      Duplicate_Folder = FALSE,
      Artifact_Count = 0,
      Four_Artifacts = FALSE,
      Canonical_Filenames = FALSE,
      Path = "",
      stringsAsFactors = FALSE
    ))
  }

  folder <- pp_dirs[idx[1]]
  files <- list.files(folder, full.names = FALSE)

  present <- file.exists(file.path(folder, EXPECTED_FILES))

  data.frame(
    PP_ID = id,
    Folder_Found = TRUE,
    Duplicate_Folder = length(idx) > 1L,
    Artifact_Count = sum(present),
    Four_Artifacts = all(present),
    Canonical_Filenames = all(present) &&
      length(files[files %in% EXPECTED_FILES]) == 4L,
    Path = normalizePath(folder, winslash = "/", mustWork = FALSE),
    stringsAsFactors = FALSE
  )
})

folder_audit <- do.call(rbind, folder_rows)

# ============================================================
# 2. ARTIFACT TOTALS / 239 x 4
# ============================================================

artifact_rows <- do.call(rbind, lapply(EXPECTED_FILES, function(f) {
  data.frame(
    Artifact = f,
    Count = sum(file.exists(file.path(
      pp_dirs, f
    ))),
    Expected = 239,
    PASS = sum(file.exists(file.path(pp_dirs, f))) == 239,
    stringsAsFactors = FALSE
  )
}))

# ============================================================
# 3. MANIFEST DISCOVERY + RECONCILIATION
# ============================================================

manifest_path <- manifest_candidates[file.exists(manifest_candidates)][1]

manifest_status <- "NOT_FOUND"

manifest <- NULL
manifest_id_col <- NA_character_
manifest_path_col <- NA_character_
manifest_title_col <- NA_character_
manifest_status_col <- NA_character_
manifest_notes_col <- NA_character_

if (!is.na(manifest_path)) {

  manifest_status <- "FOUND"

  if (!requireNamespace("readxl", quietly = TRUE)) {
    manifest_status <- "FOUND_BUT_READXL_MISSING"
  } else {

    sheets <- readxl::excel_sheets(manifest_path)

    # Prefer a sheet containing PP-like data.
    sheet_scores <- vapply(sheets, function(s) {
      z <- tryCatch(
        readxl::read_excel(manifest_path, sheet = s, n_max = 20),
        error = function(e) NULL
      )
      if (is.null(z)) return(0)
      sum(vapply(names(z), function(n)
        grepl("pp|population|package|path|title|status",
              normalize(n), perl = TRUE), logical(1)))
    }, numeric(1))

    sheet <- sheets[which.max(sheet_scores)]

    manifest <- readxl::read_excel(
      manifest_path,
      sheet = sheet
    )

    nms <- names(manifest)

    manifest_id_col <- find_column(nms, c(
      "^pp[ _-]*id$",
      "population.*package.*id",
      "package.*id"
    ))

    manifest_path_col <- find_column(nms, c(
      "^path$",
      "repository.*path",
      "package.*path",
      "folder.*path",
      "relative.*path"
    ))

    manifest_title_col <- find_column(nms, c(
      "^title$",
      "package.*title",
      "population.*title"
    ))

    manifest_status_col <- find_column(nms, c(
      "^status$",
      "aggregate.*verification.*status",
      "verification.*status"
    ))

    manifest_notes_col <- find_column(nms, c(
      "^notes?$",
      "aggregate.*verification.*notes",
      "verification.*notes"
    ))
  }
}

manifest_audit <- data.frame(
  Manifest_Path = ifelse(is.na(manifest_path), "", manifest_path),
  Manifest_Status = manifest_status,
  Sheet = ifelse(exists("sheet"), sheet, ""),
  PP_ID_Column = manifest_id_col,
  Path_Column = manifest_path_col,
  Title_Column = manifest_title_col,
  Status_Column = manifest_status_col,
  Notes_Column = manifest_notes_col,
  stringsAsFactors = FALSE
)

manifest_rows <- data.frame()

if (!is.null(manifest) && !is.na(manifest_id_col)) {

  mids <- as.character(manifest[[manifest_id_col]])
  mids <- trimws(mids)

  manifest_rows <- data.frame(
    Manifest_Row = seq_len(nrow(manifest)),
    PP_ID = mids,
    stringsAsFactors = FALSE
  )

  manifest_rows$PP_ID_VALID <- manifest_rows$PP_ID %in% EXPECTED_PP_IDS

  if (!is.na(manifest_path_col)) {
    manifest_rows$Manifest_Path <- as.character(manifest[[manifest_path_col]])
  } else {
    manifest_rows$Manifest_Path <- ""
  }

  if (!is.na(manifest_title_col)) {
    manifest_rows$Manifest_Title <- as.character(manifest[[manifest_title_col]])
  } else {
    manifest_rows$Manifest_Title <- ""
  }

  if (!is.na(manifest_status_col)) {
    manifest_rows$Manifest_Status <- as.character(manifest[[manifest_status_col]])
  } else {
    manifest_rows$Manifest_Status <- ""
  }

  if (!is.na(manifest_notes_col)) {
    manifest_rows$Manifest_Notes <- as.character(manifest[[manifest_notes_col]])
  } else {
    manifest_rows$Manifest_Notes <- ""
  }

  manifest_rows$PP_ID_VALID <- manifest_rows$PP_ID %in% EXPECTED_PP_IDS

  manifest_ids <- unique(manifest_rows$PP_ID[manifest_rows$PP_ID_VALID])

  manifest_rows$Folder_Found <- manifest_rows$PP_ID %in% folder_audit$PP_ID[
    folder_audit$Folder_Found
  ]

  manifest_rows$Folder_Path <- folder_audit$Path[
    match(manifest_rows$PP_ID, folder_audit$PP_ID)
  ]

  # Path reconciliation is intentionally tolerant:
  # compare normalized slash form and accept either the manifest's full
  # repository-relative path or its basename/folder path.
  manifest_rows$Path_Matches_Folder <- NA

  for (i in seq_len(nrow(manifest_rows))) {
    mp <- normalize(as.character(manifest_rows$Manifest_Path[i]))
    fp <- normalize(as.character(manifest_rows$Folder_Path[i]))

    if (!nzchar(mp) || !nzchar(fp)) {
      manifest_rows$Path_Matches_Folder[i] <- NA
    } else {
      mp2 <- gsub("\\\\", "/", mp)
      fp2 <- gsub("\\\\", "/", fp)
      manifest_rows$Path_Matches_Folder[i] <-
        grepl(gsub("([.|()\\[\\]{}*+?^$\\\\])", "\\\\\\1", basename(fp2)),
              mp2, perl = TRUE) ||
        grepl(
          gsub("([.|()\\[\\]{}*+?^$\\\\])", "\\\\\\1", fp2),
          mp2, perl = TRUE
        ) ||
        basename(mp2) == basename(fp2)
    }
  }
}

# ============================================================
# 4. STATUS / NOTES RECONCILIATION
# ============================================================

status_audit <- data.frame()

if (nrow(manifest_rows)) {

  status_norm <- normalize(manifest_rows$Manifest_Status)
  notes_norm <- normalize(manifest_rows$Manifest_Notes)

  # At this stage PENDING is expected because Layer 3 has just been completed.
  # The audit reports the distribution rather than forcing a status.
  status_audit <- data.frame(
    PP_ID = manifest_rows$PP_ID,
    Status = manifest_rows$Manifest_Status,
    Notes = manifest_rows$Manifest_Notes,
    Status_is_PENDING = status_norm == "pending",
    Notes_mentions_aggregate_verification =
      grepl("aggregate verification", notes_norm, fixed = TRUE),
    stringsAsFactors = FALSE
  )
}

# ============================================================
# 5. GIT AUDIT
# ============================================================

run_cmd <- function(cmd) {
  tryCatch(
    system2("git", args = cmd, stdout = TRUE, stderr = TRUE),
    error = function(e) paste("ERROR:", conditionMessage(e))
  )
}

git_ok <- dir.exists(file.path(REPO_ROOT, ".git"))

git_head <- ""
git_status <- character()
git_remote <- character()
git_pp_files <- character()

if (git_ok) {
  git_head <- paste(run_cmd(c("-C", REPO_ROOT, "rev-parse", "HEAD")),
                    collapse = "\n")

  git_status <- run_cmd(c("-C", REPO_ROOT, "status", "--short"))

  git_remote <- run_cmd(c("-C", REPO_ROOT, "remote", "-v"))

  git_pp_files <- run_cmd(c(
    "-C", REPO_ROOT,
    "ls-tree", "-r", "--name-only", "HEAD",
    "--", "03_Clinical_Knowledge/population/population_packages/"
  ))
}

git_head_clean <- trimws(git_head)

git_pp_file_lines <- git_pp_files[
  grepl(
    "03_Clinical_Knowledge/population/population_packages/",
    git_pp_files,
    fixed = TRUE
  )
]

git_artifact_counts <- data.frame(
  Artifact = EXPECTED_FILES,
  Count = vapply(EXPECTED_FILES, function(f)
    sum(grepl(paste0("/", gsub("\\.", "\\.", f), "$"),
              git_pp_file_lines, perl = TRUE)),
    numeric(1)
  ),
  Expected = 239,
  stringsAsFactors = FALSE
)

git_artifact_counts$PASS <- git_artifact_counts$Count == 239

# ============================================================
# 6. FINAL RECONCILIATION
# ============================================================

layer3_pass <- all(
  folder_audit$Folder_Found,
  !folder_audit$Duplicate_Folder,
  folder_audit$Four_Artifacts,
  folder_audit$Canonical_Filenames
) && all(artifact_rows$PASS)

manifest_id_pass <- FALSE
manifest_count_pass <- FALSE
manifest_duplicates_pass <- FALSE
manifest_path_pass <- FALSE
manifest_status_ready <- FALSE

if (nrow(manifest_rows)) {

  manifest_id_pass <-
    all(manifest_rows$PP_ID_VALID) &&
    all(manifest_rows$PP_ID != "") &&
    all(manifest_rows$Folder_Found)

  manifest_count_pass <-
    length(unique(manifest_rows$PP_ID[manifest_rows$PP_ID_VALID])) == 239

  manifest_duplicates_pass <-
    !any(duplicated(manifest_rows$PP_ID[
      manifest_rows$PP_ID_VALID
    ]))

  if (!is.na(manifest_path_col)) {
    manifest_path_pass <-
      sum(manifest_rows$Path_Matches_Folder == TRUE, na.rm = TRUE) == 239
  } else {
    manifest_path_pass <- FALSE
  }

  if (!is.na(manifest_status_col)) {
    manifest_status_ready <- all(
      manifest_rows$PP_ID %in% EXPECTED_PP_IDS
    )
  }
}

git_commit_pass <- git_head_clean == EXPECTED_COMMIT

git_remote_pass <- any(
  grepl(
    gsub("([.|()\\[\\]{}*+?^$\\\\])", "\\\\\\1", EXPECTED_REMOTE),
    git_remote,
    fixed = FALSE,
    perl = TRUE
  )
)

git_artifact_pass <- all(git_artifact_counts$PASS)

# Working tree is allowed to contain audit/working files, but we report it.
git_clean <- length(git_status) == 0L

phase3_completion_objective_pass <-
  layer3_pass &&
  manifest_id_pass &&
  manifest_count_pass &&
  manifest_duplicates_pass &&
  manifest_path_pass &&
  git_commit_pass &&
  git_remote_pass &&
  git_artifact_pass

# Phase 4 readiness is deliberately split:
# objective repository readiness can PASS even if governance/operations
# fields are still marked pending in the manifest.
phase4_readiness_objective <- phase3_completion_objective_pass

# ============================================================
# 7. OUTPUT TABLES
# ============================================================

final_matrix <- data.frame(
  Gate = c(
    "Layer 3 objective integrity",
    "239 PP folders present",
    "239 x 4 canonical artifacts",
    "Manifest found",
    "Manifest contains 239 unique PP IDs",
    "Manifest PP IDs reconcile to repository folders",
    "Manifest paths reconcile to repository folders",
    "Git HEAD is expected Phase 3 commit",
    "Git remote is official repository",
    "Git contains 239 x 4 Gold artifacts",
    "Git working tree clean"
  ),
  Result = c(
    layer3_pass,
    all(folder_audit$Folder_Found),
    all(artifact_rows$PASS),
    !is.na(manifest_path),
    manifest_count_pass,
    manifest_id_pass,
    manifest_path_pass,
    git_commit_pass,
    git_remote_pass,
    git_artifact_pass,
    git_clean
  ),
  stringsAsFactors = FALSE
)

summary_lines <- c(
  "============================================================",
  "PHASE 3 COMPLETION & PHASE 4 READINESS AUDIT v1",
  "============================================================",
  paste0("Repository: ", REPO_ROOT),
  paste0("PP root: ", PP_ROOT),
  "",
  paste0("Expected PP count: 239"),
  paste0("PP folders found: ", sum(folder_audit$Folder_Found), " / 239"),
  paste0("Complete 4-artifact packages: ",
         sum(folder_audit$Four_Artifacts), " / 239"),
  paste0("Canonical artifact counts: ",
         paste(artifact_rows$Count, collapse = " / ")),
  "",
  paste0("Layer 3 objective integrity: ",
         ifelse(layer3_pass, "PASS", "FAIL")),
  "",
  paste0("Manifest status: ", manifest_status),
  paste0("Manifest PP ID reconciliation: ",
         ifelse(manifest_id_pass, "PASS", "FAIL")),
  paste0("Manifest unique PP count: ",
         ifelse(manifest_count_pass, "PASS", "FAIL")),
  paste0("Manifest duplicate IDs: ",
         ifelse(manifest_duplicates_pass, "PASS", "FAIL")),
  paste0("Manifest path reconciliation: ",
         ifelse(manifest_path_pass, "PASS", "FAIL")),
  "",
  paste0("Git HEAD: ", git_head_clean),
  paste0("Expected Phase 3 commit: ", EXPECTED_COMMIT),
  paste0("Git commit reconciliation: ",
         ifelse(git_commit_pass, "PASS", "FAIL")),
  paste0("Git remote reconciliation: ",
         ifelse(git_remote_pass, "PASS", "FAIL")),
  paste0("Git 239 x 4 artifact reconciliation: ",
         ifelse(git_artifact_pass, "PASS", "FAIL")),
  paste0("Git working tree clean: ",
         ifelse(git_clean, "PASS", "REPORT ONLY")),
  "",
  paste0("PHASE 3 COMPLETION OBJECTIVE GATE: ",
         ifelse(phase3_completion_objective_pass, "PASS", "FAIL")),
  paste0("PHASE 4 OBJECTIVE READINESS: ",
         ifelse(phase4_readiness_objective, "READY", "NOT READY")),
  "",
  "Note:",
  "Git working-tree cleanliness is reported separately.",
  "Untracked working/audit files do not invalidate the immutable",
  "Phase 3 commit itself, provided the expected commit contains",
  "the verified 239 x 4 Gold artifacts.",
  "============================================================"
)

# ============================================================
# 8. WRITE FILES
# ============================================================

safe_csv(folder_audit,
         file.path(AUDIT_ROOT, "01_PP_Folder_Reconciliation.csv"))

safe_csv(artifact_rows,
         file.path(AUDIT_ROOT, "02_Artifact_Counts.csv"))

safe_csv(manifest_audit,
         file.path(AUDIT_ROOT, "03_Manifest_Metadata.csv"))

if (nrow(manifest_rows)) {
  safe_csv(manifest_rows,
           file.path(AUDIT_ROOT, "04_Manifest_Reconciliation.csv"))
}

if (nrow(status_audit)) {
  safe_csv(status_audit,
           file.path(AUDIT_ROOT, "05_Manifest_Status_Audit.csv"))
}

safe_csv(git_artifact_counts,
         file.path(AUDIT_ROOT, "06_Git_Artifact_Counts.csv"))

safe_csv(final_matrix,
         file.path(AUDIT_ROOT, "07_Final_Gate_Matrix.csv"))

writeLines(summary_lines,
           file.path(AUDIT_ROOT, "08_Final_Summary.txt"),
           useBytes = TRUE)

writeLines(
  c(
    "GIT HEAD",
    git_head_clean,
    "",
    "GIT STATUS",
    git_status,
    "",
    "GIT REMOTE",
    git_remote
  ),
  file.path(AUDIT_ROOT, "09_Git_State.txt"),
  useBytes = TRUE
)

# ============================================================
# 9. CONSOLE
# ============================================================

cat("\n")
cat(paste(summary_lines, collapse = "\n"))
cat("\n\nOutput directory:\n", AUDIT_ROOT, "\n", sep = "")
cat("\nPlease provide these files for final review:\n")
cat("01_PP_Folder_Reconciliation.csv\n")
cat("02_Artifact_Counts.csv\n")
cat("03_Manifest_Metadata.csv\n")
cat("04_Manifest_Reconciliation.csv (if created)\n")
cat("05_Manifest_Status_Audit.csv (if created)\n")
cat("06_Git_Artifact_Counts.csv\n")
cat("07_Final_Gate_Matrix.csv\n")
cat("08_Final_Summary.txt\n")
cat("09_Git_State.txt\n")
