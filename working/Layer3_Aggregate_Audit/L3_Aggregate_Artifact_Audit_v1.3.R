
# ============================================================
# PHASE 3C — LAYER 3 AGGREGATE ARTIFACT AUDIT
# Safe Medical AI System for Oncology Patient Education
#
# Purpose:
#   Aggregate structural / metadata / traceability audit for
#   PP-0001 -> PP-0239 (239 Population Packages / 956 artifacts)
#
# Important:
#   - READ-ONLY audit of the Population Packages.
#   - Does NOT modify any Gold Markdown.
#   - Does NOT change Git.
#   - Does NOT replace clinical expert review.
#   - Produces CSV/TXT audit evidence for strategist review.
#
# Requirements:
#   - Base R only. No extra packages required.
#   - Run this script from the repository root:
#       safe-medical-ai-oncology/
# ============================================================

options(stringsAsFactors = FALSE, warn = 1)

# ---------- 1. CONFIGURATION ----------

REPO_ROOT <- "D:/GIT hub/safe-medical-ai-oncology"
# If your repository is stored elsewhere, change ONLY the line above.
REPO_ROOT <- normalizePath(REPO_ROOT, winslash = "/", mustWork = TRUE)

PP_ROOT <- file.path(
  REPO_ROOT,
  "03_Clinical_Knowledge",
  "population",
  "population_packages"
)

OUTPUT_DIR <- file.path(
  REPO_ROOT,
  "working",
  "Layer3_Aggregate_Audit"
)

EXPECTED_PP_IDS <- sprintf("PP-%04d", 1:239)

EXPECTED_FILES <- c(
  "01_CKO.md",
  "02_KNOWLEDGE_PASSPORT.md",
  "03_PRIMARY_EVIDENCE_PACKAGE.md",
  "04_QA_REPORT.md"
)

EXPECTED_VERSION <- "1.0.0"

# ---------- 2. BASIC HELPERS ----------

safe_read <- function(path) {
  if (!file.exists(path)) return("")
  x <- tryCatch(
    readLines(path, encoding = "UTF-8", warn = FALSE),
    error = function(e) {
      # Fallback for unusual Windows encoding situations
      tryCatch(
        readLines(path, encoding = "unknown", warn = FALSE),
        error = function(e2) character()
      )
    }
  )
  paste(enc2utf8(x), collapse = "\n")
}

has_text <- function(text, pattern) {
  # Never allow NA/invalid text to propagate into if()/all() logic.
  if (length(text) != 1L || is.na(text) || !nzchar(text)) return(FALSE)
  out <- tryCatch(
    grepl(pattern, text, ignore.case = TRUE, perl = TRUE),
    error = function(e) FALSE
  )
  isTRUE(out)
}

has_any_text <- function(text, patterns) {
  any(vapply(patterns, function(p) has_text(text, p), logical(1)))
}

# Force every audit predicate to a strict TRUE/FALSE.
# This prevents R errors such as:
# "missing value where TRUE/FALSE needed"
safe_bool <- function(x) {
  isTRUE(x)
}

all_true <- function(...) {
  vals <- list(...)
  all(vapply(vals, safe_bool, logical(1)))
}

count_pattern <- function(text, pattern) {
  if (length(text) != 1L || is.na(text) || !nzchar(text)) return(0L)
  m <- tryCatch(
    gregexpr(pattern, text, ignore.case = TRUE, perl = TRUE)[[1]],
    error = function(e) -1L
  )
  if (length(m) == 1L && m[1] == -1L) return(0L)
  length(m)
}

extract_md_field <- function(text, field) {
  # Typical governed metadata:
  # | PP ID | PP-0185 |
  # | Version | 1.0.0 |
  # | Final Status | PASS — GOLD — READY FOR INTEGRATION |
  pat <- paste0(
    "^\\s*\\|\\s*",
    "\\Q", field, "\\E",
    "\\s*\\|\\s*(.*?)\\s*\\|\\s*$"
  )
  lines <- strsplit(text, "\n", fixed = TRUE)[[1]]
  hit <- grep(pat, lines, ignore.case = TRUE, perl = TRUE, value = TRUE)
  if (length(hit) == 0L) return(NA_character_)
  sub(pat, "\\1", hit[1], ignore.case = TRUE, perl = TRUE)
}

extract_first_field <- function(text, fields) {
  for (f in fields) {
    v <- extract_md_field(text, f)
    if (!is.na(v) && nzchar(trimws(v))) return(trimws(v))
  }
  NA_character_
}

heading_present <- function(text, phrase) {
  # Structural heading check. We intentionally allow # / ## / ###.
  has_text(text, paste0("(?m)^#{1,3}\\s*", phrase))
}

heading_any <- function(text, phrases) {
  any(vapply(phrases, function(p) heading_present(text, p), logical(1)))
}

section_line_count <- function(text, start_phrase) {
  lines <- strsplit(text, "\n", fixed = TRUE)[[1]]
  idx <- grep(
    paste0("^#{1,3}\\s*", start_phrase),
    lines,
    ignore.case = TRUE,
    perl = TRUE
  )
  if (length(idx) == 0L) return(NA_integer_)
  start <- idx[1]
  next_heading <- grep("^#{1,3}\\s+", lines[(start + 1):length(lines)])
  if (length(next_heading) == 0L) {
    end <- length(lines)
  } else {
    end <- start + next_heading[1] - 1L
  }
  max(0L, end - start)
}

count_markdown_table_rows <- function(text, section_phrase) {
  lines <- strsplit(text, "\n", fixed = TRUE)[[1]]
  idx <- grep(
    paste0("^#{1,3}\\s*", section_phrase),
    lines,
    ignore.case = TRUE,
    perl = TRUE
  )
  if (length(idx) == 0L) return(NA_integer_)
  start <- idx[1]
  next_heading <- grep("^#{1,3}\\s+", lines[(start + 1):length(lines)])
  if (length(next_heading) == 0L) {
    end <- length(lines)
  } else {
    end <- start + next_heading[1] - 1L
  }
  block <- lines[start:end]
  table_lines <- grep("^\\s*\\|", block, value = TRUE)
  # subtract header + separator when present
  n <- length(table_lines)
  if (n >= 2L) n <- n - 2L
  max(0L, n)
}

first_pp_id <- function(x) {
  m <- regexpr("PP-[0-9]{4}", x, perl = TRUE)
  if (m[1] == -1L) return(NA_character_)
  regmatches(x, m)
}

check_required_sections <- function(text, artifact) {
  if (artifact == "CKO") {
    required <- c(
      "Metadata",
      "Educational Objectives",
      "Scope",
      "Clinical Knowledge Blocks",
      "Key Messages",
      "Knowledge Graph",
      "Revision History"
    )
  } else if (artifact == "KP") {
    required <- c(
      "Identity",
      "Knowledge Classification",
      "Patient Journey Classification",
      "Primary Runtime Role",
      "Secondary Runtime Roles",
      "Typical Trigger Questions",
      "Retrieval Priority",
      "Knowledge Graph",
      "Clinical Scope",
      "Explicitly Excluded",
      "Authoritative Sources",
      "Evidence Classification",
      "Intended Knowledge Boundaries",
      "Governance Metadata",
      "Version Control",
      "Change History",
      "Future Update Triggers",
      "Quality Status",
      "Final Status"
    )
  } else if (artifact == "EP") {
    required <- c(
      "Identity",
      "Clinical Question",
      "Educational Intent",
      "Scope",
      "Primary Evidence Sources",
      "Supporting Sources",
      "Evidence Hierarchy",
      "Evidence Matrix",
      "Clinical Claims Summary",
      "Evidence Gaps",
      "Out-of-Scope Topics",
      "Future Update Triggers",
      "Source Traceability",
      "Boundary Verification",
      "Final Evidence Status"
    )
  } else {
    required <- c(
      "Identity",
      "QA Objective",
      "Layer 1 — Content QA",
      "Layer 2 — Clinical QA",
      "Layer 3 — Educational QA",
      "Layer 4 — Governance QA",
      "Cross-Artifact Consistency Check",
      "Final QA Decision",
      "Final Status"
    )
  }

  present <- vapply(
    required,
    function(x) heading_present(text, x),
    logical(1)
  )

  # Treat NA as a failed check, never as an indeterminate value.
  present[is.na(present)] <- FALSE

  list(
    pass = all(present),
    missing = paste(required[!present], collapse = " | ")
  )
}

# ---------- 3. PRE-FLIGHT ----------

if (!dir.exists(PP_ROOT)) {
  stop(
    paste0(
      "\nSTOP: Population Package directory not found.\n\n",
      "Expected:\n", PP_ROOT, "\n\n",
      "Make sure you opened/run the script from the ",
      "safe-medical-ai-oncology repository root.\n"
    )
  )
}

if (!dir.exists(OUTPUT_DIR)) {
  dir.create(OUTPUT_DIR, recursive = TRUE, showWarnings = FALSE)
}

# ---------- 4. DISCOVER PP FOLDERS ----------

pp_dirs <- list.dirs(PP_ROOT, recursive = FALSE, full.names = TRUE)
pp_dirs <- pp_dirs[basename(pp_dirs) != ""]

folder_ids <- vapply(
  basename(pp_dirs),
  first_pp_id,
  character(1)
)

# Remove folders that do not look like PP folders
valid_idx <- !is.na(folder_ids)
pp_dirs <- pp_dirs[valid_idx]
folder_ids <- folder_ids[valid_idx]

# ---------- 5. AUDIT EACH PP ----------

rows <- vector("list", length(EXPECTED_PP_IDS))
depth_rows <- vector("list", length(EXPECTED_PP_IDS))

for (i in seq_along(EXPECTED_PP_IDS)) {

  pp_id <- EXPECTED_PP_IDS[i]

  matches <- which(folder_ids == pp_id)

  if (length(matches) == 0L) {

    rows[[i]] <- data.frame(
      PP_ID = pp_id,
      Folder_Found = FALSE,
      Folder_Name = NA_character_,
      CKO_Exists = FALSE,
      KP_Exists = FALSE,
      EP_Exists = FALSE,
      QA_Exists = FALSE,
      Four_Artifacts = FALSE,
      CKO_ID_OK = FALSE,
      KP_ID_OK = FALSE,
      EP_ID_OK = FALSE,
      QA_ID_OK = FALSE,
      Version_OK = FALSE,
      Title_OK = FALSE,
      CKO_Structure_OK = FALSE,
      KP_Structure_OK = FALSE,
      EP_Structure_OK = FALSE,
      QA_Structure_OK = FALSE,
      Boundary_OK = FALSE,
      Evidence_Traceability_OK = FALSE,
      QA_Final_Status_OK = FALSE,
      Cross_Artifact_Consistency_OK = FALSE,
      Aggregate_Row_PASS = FALSE,
      Exceptions = "PP folder not found",
      stringsAsFactors = FALSE
    )

    depth_rows[[i]] <- data.frame(
      PP_ID = pp_id,
      CKO_Characters = NA_integer_,
      CKO_Headings = NA_integer_,
      CKO_Knowledge_Blocks = NA_integer_,
      KP_Characters = NA_integer_,
      KP_Headings = NA_integer_,
      EP_Characters = NA_integer_,
      EP_Headings = NA_integer_,
      EP_Evidence_Matrix_Rows = NA_integer_,
      QA_Characters = NA_integer_,
      QA_Headings = NA_integer_,
      QA_PASS_Mentions = NA_integer_,
      stringsAsFactors = FALSE
    )

    next
  }

  if (length(matches) > 1L) {
    folder <- pp_dirs[matches[1]]
    duplicate_flag <- TRUE
  } else {
    folder <- pp_dirs[matches]
    duplicate_flag <- FALSE
  }

  folder_name <- basename(folder)

  files <- file.path(folder, EXPECTED_FILES)
  names(files) <- c("CKO", "KP", "EP", "QA")

  exists <- file.exists(files)

  texts <- lapply(files, safe_read)

  # ----- identity / version / title -----

  cko_pp <- extract_first_field(texts$CKO, c("PP ID", "Population Package ID"))
  kp_pp  <- extract_first_field(texts$KP,  c("PP ID", "Population Package ID"))
  ep_pp  <- extract_first_field(texts$EP,  c("PP ID", "Population Package ID"))
  qa_pp  <- extract_first_field(texts$QA,  c("PP ID", "Population Package ID"))

  cko_ver <- extract_first_field(texts$CKO, c("Version"))
  kp_ver  <- extract_first_field(texts$KP,  c("Version"))
  ep_ver  <- extract_first_field(texts$EP,  c("Version"))
  qa_ver  <- extract_first_field(texts$QA,  c("Version"))

  titles <- c(
    extract_first_field(texts$CKO, c("Title")),
    extract_first_field(texts$KP,  c("Title")),
    extract_first_field(texts$EP,  c("Title")),
    extract_first_field(texts$QA,  c("Title"))
  )

  title_ok <- all(!is.na(titles)) &&
    length(unique(titles)) == 1L

  version_ok <- all(
    !is.na(c(cko_ver, kp_ver, ep_ver, qa_ver)),
    c(cko_ver, kp_ver, ep_ver, qa_ver) == EXPECTED_VERSION
  )

  id_values <- c(cko_pp, kp_pp, ep_pp, qa_pp)
  ids_ok <- all(!is.na(id_values) & id_values == pp_id)

  # ----- structural checks -----

  cko_struct <- safe_bool(exists["CKO"]) &&
    safe_bool(check_required_sections(texts$CKO, "CKO")$pass)

  kp_struct <- safe_bool(exists["KP"]) &&
    safe_bool(check_required_sections(texts$KP, "KP")$pass)

  ep_struct <- safe_bool(exists["EP"]) &&
    safe_bool(check_required_sections(texts$EP, "EP")$pass)

  qa_struct <- safe_bool(exists["QA"]) &&
    safe_bool(check_required_sections(texts$QA, "QA")$pass)

  # Final defensive normalization: structural predicates must be TRUE/FALSE.
  cko_struct <- safe_bool(cko_struct)
  kp_struct  <- safe_bool(kp_struct)
  ep_struct  <- safe_bool(ep_struct)
  qa_struct  <- safe_bool(qa_struct)

  # ----- boundary / evidence / QA checks -----

  boundary_ok <- all(
    has_text(texts$KP, "Intended Knowledge Boundaries"),
    has_text(texts$KP, "Core"),
    has_text(texts$KP, "Supporting"),
    has_text(texts$KP, "Explicitly Excluded"),
    has_text(texts$KP, "Delegat"),
    has_text(texts$EP, "Boundary Verification"),
    has_text(texts$QA, "Boundary Completeness")
  )

  evidence_traceability_ok <- all(
    has_text(texts$EP, "Evidence Matrix"),
    has_text(texts$EP, "Evidence Hierarchy"),
    has_text(texts$EP, "Source Traceability"),
    has_text(texts$EP, "Primary Evidence Sources")
  )

  qa_final_status <- has_text(
    texts$QA,
    "PASS\\s*[—-]\\s*GOLD\\s*[—-]\\s*READY FOR INTEGRATION"
  )

  # QA cross-artifact consistency section should exist and contain PASS
  cross_artifact_ok <- all(
    has_text(texts$QA, "Cross-Artifact Consistency Check"),
    has_text(texts$QA, "PP ID consistent across all artifacts"),
    has_text(texts$QA, "Version consistent"),
    has_text(texts$QA, "Scope consistent"),
    has_text(texts$QA, "Boundary consistent"),
    has_text(texts$QA, "QA status consistent")
  )

  # ----- exception collection -----

  exceptions <- character()

  if (duplicate_flag) {
    exceptions <- c(exceptions, "Duplicate PP folder ID")
  }

  if (!all(exists)) {
    exceptions <- c(
      exceptions,
      paste0("Missing artifact(s): ",
             paste(names(exists)[!exists], collapse = ", "))
    )
  }

  if (!ids_ok) {
    exceptions <- c(exceptions, "PP ID mismatch/missing in one or more artifacts")
  }

  if (!version_ok) {
    exceptions <- c(exceptions, "Version missing or not 1.0.0 across all artifacts")
  }

  if (!title_ok) {
    exceptions <- c(exceptions, "Title missing or inconsistent across artifacts")
  }

  if (!safe_bool(cko_struct)) exceptions <- c(exceptions, "CKO structural check failed")
  if (!safe_bool(kp_struct)) exceptions <- c(exceptions, "KP structural check failed")
  if (!safe_bool(ep_struct)) exceptions <- c(exceptions, "EP structural check failed")
  if (!safe_bool(qa_struct)) exceptions <- c(exceptions, "QA structural check failed")

  if (!safe_bool(boundary_ok)) {
    exceptions <- c(exceptions, "Boundary structure check failed")
  }

  if (!safe_bool(evidence_traceability_ok)) {
    exceptions <- c(exceptions, "Evidence traceability structure check failed")
  }

  if (!safe_bool(qa_final_status)) {
    exceptions <- c(exceptions, "QA Final Status is not PASS — GOLD — READY FOR INTEGRATION")
  }

  if (!safe_bool(cross_artifact_ok)) {
    exceptions <- c(exceptions, "QA cross-artifact consistency evidence incomplete")
  }

  all_four <- all(exists)

  aggregate_pass <- all_true(
    all_four,
    ids_ok,
    version_ok,
    title_ok,
    cko_struct,
    kp_struct,
    ep_struct,
    qa_struct,
    boundary_ok,
    evidence_traceability_ok,
    qa_final_status,
    cross_artifact_ok
  )

  rows[[i]] <- data.frame(
    PP_ID = pp_id,
    Folder_Found = TRUE,
    Folder_Name = folder_name,
    CKO_Exists = exists["CKO"],
    KP_Exists = exists["KP"],
    EP_Exists = exists["EP"],
    QA_Exists = exists["QA"],
    Four_Artifacts = all_four,
    CKO_ID_OK = identical(cko_pp, pp_id),
    KP_ID_OK = identical(kp_pp, pp_id),
    EP_ID_OK = identical(ep_pp, pp_id),
    QA_ID_OK = identical(qa_pp, pp_id),
    Version_OK = version_ok,
    Title_OK = title_ok,
    CKO_Structure_OK = cko_struct,
    KP_Structure_OK = kp_struct,
    EP_Structure_OK = ep_struct,
    QA_Structure_OK = qa_struct,
    Boundary_OK = boundary_ok,
    Evidence_Traceability_OK = evidence_traceability_ok,
    QA_Final_Status_OK = qa_final_status,
    Cross_Artifact_Consistency_OK = cross_artifact_ok,
    Aggregate_Row_PASS = aggregate_pass,
    Exceptions = if (length(exceptions) == 0L) "" else paste(exceptions, collapse = " | "),
    stringsAsFactors = FALSE
  )

  # ----- depth / richness metrics (REPORT ONLY, NOT PASS/FAIL) -----

  depth_rows[[i]] <- data.frame(
    PP_ID = pp_id,
    CKO_Characters = nchar(texts$CKO),
    CKO_Headings = count_pattern(texts$CKO, "(?m)^#{1,3}\\s+"),
    CKO_Knowledge_Blocks = count_pattern(texts$CKO, "(?m)^##\\s+Knowledge Block"),
    KP_Characters = nchar(texts$KP),
    KP_Headings = count_pattern(texts$KP, "(?m)^#{1,3}\\s+"),
    EP_Characters = nchar(texts$EP),
    EP_Headings = count_pattern(texts$EP, "(?m)^#{1,3}\\s+"),
    EP_Evidence_Matrix_Rows = count_markdown_table_rows(texts$EP, "Evidence Matrix"),
    QA_Characters = nchar(texts$QA),
    QA_Headings = count_pattern(texts$QA, "(?m)^#{1,3}\\s+"),
    QA_PASS_Mentions = count_pattern(texts$QA, "\\bPASS\\b"),
    stringsAsFactors = FALSE
  )
}

# ---------- 6. COMBINE RESULTS ----------

detail <- do.call(rbind, rows)
depth <- do.call(rbind, depth_rows)

# ---------- 7. PACKAGE-LEVEL / POPULATION-LEVEL SUMMARY ----------

n_pp <- nrow(detail)

summary_lines <- c(
  "PHASE 3C — LAYER 3 AGGREGATE ARTIFACT AUDIT",
  "============================================================",
  paste0("Repository root: ", REPO_ROOT),
  paste0("Population Package root: ", PP_ROOT),
  "",
  paste0("Expected PP count: ", length(EXPECTED_PP_IDS)),
  paste0("Discovered/audited PP rows: ", n_pp),
  paste0("Expected artifacts: ", length(EXPECTED_PP_IDS) * length(EXPECTED_FILES)),
  "",
  paste0("PP folders found: ", sum(detail$Folder_Found), " / ", length(EXPECTED_PP_IDS)),
  paste0("4-artifact complete packages: ", sum(detail$Four_Artifacts), " / ", length(EXPECTED_PP_IDS)),
  paste0("PP ID consistency PASS: ", sum(
    detail$CKO_ID_OK & detail$KP_ID_OK & detail$EP_ID_OK & detail$QA_ID_OK
  ), " / ", length(EXPECTED_PP_IDS)),
  paste0("Version consistency PASS: ", sum(detail$Version_OK), " / ", length(EXPECTED_PP_IDS)),
  paste0("Title consistency PASS: ", sum(detail$Title_OK), " / ", length(EXPECTED_PP_IDS)),
  paste0("CKO structure PASS: ", sum(detail$CKO_Structure_OK), " / ", length(EXPECTED_PP_IDS)),
  paste0("KP structure PASS: ", sum(detail$KP_Structure_OK), " / ", length(EXPECTED_PP_IDS)),
  paste0("EP structure PASS: ", sum(detail$EP_Structure_OK), " / ", length(EXPECTED_PP_IDS)),
  paste0("QA structure PASS: ", sum(detail$QA_Structure_OK), " / ", length(EXPECTED_PP_IDS)),
  paste0("Boundary structure PASS: ", sum(detail$Boundary_OK), " / ", length(EXPECTED_PP_IDS)),
  paste0("Evidence traceability structure PASS: ", sum(detail$Evidence_Traceability_OK), " / ", length(EXPECTED_PP_IDS)),
  paste0("QA final status PASS: ", sum(detail$QA_Final_Status_OK), " / ", length(EXPECTED_PP_IDS)),
  paste0("Cross-artifact consistency evidence PASS: ", sum(detail$Cross_Artifact_Consistency_OK), " / ", length(EXPECTED_PP_IDS)),
  "",
  paste0("AGGREGATE ROW PASS: ", sum(detail$Aggregate_Row_PASS), " / ", length(EXPECTED_PP_IDS)),
  "",
  "IMPORTANT:",
  "- Depth metrics are reported only; they are NOT automatically converted into PASS/FAIL.",
  "- This script audits structural/metadata/traceability evidence and does not replace clinical judgment.",
  "- Clinical accuracy and patient-safety claims remain governed by the approved QA process.",
  ""
)

if (sum(detail$Aggregate_Row_PASS) == length(EXPECTED_PP_IDS)) {
  summary_lines <- c(
    summary_lines,
    "PROVISIONAL AUTOMATED RESULT: ALL 239 PP ROWS PASSED THE AUTOMATED AGGREGATE CHECKS."
  )
} else {
  summary_lines <- c(
    summary_lines,
    "PROVISIONAL AUTOMATED RESULT: EXCEPTIONS REQUIRE REVIEW."
  )
}

# ---------- 8. WRITE OUTPUTS ----------

detail_file <- file.path(OUTPUT_DIR, "L3_Aggregate_Audit_Detail.csv")
depth_file <- file.path(OUTPUT_DIR, "L3_Aggregate_Audit_Depth_Metrics.csv")
exception_file <- file.path(OUTPUT_DIR, "L3_Aggregate_Audit_Exceptions.csv")
summary_file <- file.path(OUTPUT_DIR, "L3_Aggregate_Audit_Summary.txt")

write.csv(detail, detail_file, row.names = FALSE, fileEncoding = "UTF-8")
write.csv(depth, depth_file, row.names = FALSE, fileEncoding = "UTF-8")

exceptions <- detail[nzchar(detail$Exceptions), ]
write.csv(exceptions, exception_file, row.names = FALSE, fileEncoding = "UTF-8")

writeLines(summary_lines, summary_file, useBytes = TRUE)

# ---------- 9. CONSOLE OUTPUT ----------

cat("\n============================================================\n")
cat("LAYER 3 AGGREGATE ARTIFACT AUDIT — COMPLETED\n")
cat("============================================================\n")
cat("PP folders audited:       ", sum(detail$Folder_Found), " / 239\n", sep = "")
cat("4-artifact complete:      ", sum(detail$Four_Artifacts), " / 239\n", sep = "")
cat("PP ID consistency:        ",
    sum(detail$CKO_ID_OK & detail$KP_ID_OK & detail$EP_ID_OK & detail$QA_ID_OK),
    " / 239\n", sep = "")
cat("Version consistency:      ", sum(detail$Version_OK), " / 239\n", sep = "")
cat("Title consistency:        ", sum(detail$Title_OK), " / 239\n", sep = "")
cat("CKO structure:            ", sum(detail$CKO_Structure_OK), " / 239\n", sep = "")
cat("KP structure:             ", sum(detail$KP_Structure_OK), " / 239\n", sep = "")
cat("EP structure:             ", sum(detail$EP_Structure_OK), " / 239\n", sep = "")
cat("QA structure:             ", sum(detail$QA_Structure_OK), " / 239\n", sep = "")
cat("Boundary structure:       ", sum(detail$Boundary_OK), " / 239\n", sep = "")
cat("Evidence traceability:    ", sum(detail$Evidence_Traceability_OK), " / 239\n", sep = "")
cat("QA final status:          ", sum(detail$QA_Final_Status_OK), " / 239\n", sep = "")
cat("Cross-artifact evidence:  ", sum(detail$Cross_Artifact_Consistency_OK), " / 239\n", sep = "")
cat("Aggregate row PASS:       ", sum(detail$Aggregate_Row_PASS), " / 239\n", sep = "")
cat("\nOutput directory:\n", OUTPUT_DIR, "\n\n", sep = "")

if (sum(detail$Aggregate_Row_PASS) == 239) {
  cat("RESULT: PROVISIONAL AUTOMATED PASS — 239/239\n")
  cat("Strategist review is still required before declaring Layer 3 PASS.\n")
} else {
  cat("RESULT: REVIEW REQUIRED — exceptions detected.\n")
  cat("Open the Exceptions CSV for PP-level findings.\n")
}

cat("\nFiles created:\n")
cat(" - ", detail_file, "\n", sep = "")
cat(" - ", depth_file, "\n", sep = "")
cat(" - ", exception_file, "\n", sep = "")
cat(" - ", summary_file, "\n", sep = "")
