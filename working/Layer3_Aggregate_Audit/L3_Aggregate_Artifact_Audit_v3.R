# ============================================================
# PHASE 3C — LAYER 3 AGGREGATE ARTIFACT AUDIT v3
# TRUE-INTEGRITY / CROSS-ARTIFACT CALIBRATED AUDIT
#
# PURPOSE
#   Verify objective repository/package integrity for PP-0001..PP-0239.
#
# IMPORTANT
#   This script is READ-ONLY.
#   It does NOT edit Gold artifacts or Git.
#   It does NOT infer clinical correctness from headings.
#   It does NOT fail a PP merely because a preferred heading/wording
#   is absent.
#
# CLASSIFICATION
#   HARD_FAIL       = objective repository/package integrity defect
#   CROSS_ARTIFACT  = objective inconsistency between artifacts
#   SEMANTIC_REVIEW = evidence exists but requires human/strategist review
#   REPORT_ONLY     = descriptive depth/richness metric
#
# HARD GATES
#   1. PP folder exists
#   2. Four canonical artifacts exist
#   3. Canonical filenames
#   4. Folder ID is PP-XXXX and belongs to expected range
#   5. Artifact-declared PP ID, when explicitly declared, is not contradictory
#   6. Artifact-declared version, when explicitly declared, is not contradictory
#   7. No duplicate PP folder IDs
#
# CROSS-ARTIFACT GATES
#   1. Explicit PP IDs, if present, agree
#   2. Explicit versions, if present, agree
#   3. Explicit titles, if present, do not contradict one another
#
# SEMANTIC REVIEW (NEVER HARD FAIL)
#   CKO: scope / knowledge / graph evidence
#   KP : governance/runtime/boundary evidence
#   EP : evidence/traceability/boundary evidence
#   QA : content/clinical/educational/governance/decision evidence
#
# DEPTH METRICS
#   REPORT ONLY.
# ============================================================

options(stringsAsFactors = FALSE, warn = 1)

# ---------- CONFIG ----------

REPO_ROOT <- "D:/GIT hub/safe-medical-ai-oncology"
REPO_ROOT <- normalizePath(REPO_ROOT, winslash = "/", mustWork = TRUE)

PP_ROOT <- file.path(
  REPO_ROOT, "03_Clinical_Knowledge", "population", "population_packages"
)

OUTPUT_DIR <- file.path(
  REPO_ROOT, "working", "Layer3_Aggregate_Audit"
)

EXPECTED_PP_IDS <- sprintf("PP-%04d", 1:239)

EXPECTED_FILES <- c(
  "01_CKO.md",
  "02_KNOWLEDGE_PASSPORT.md",
  "03_PRIMARY_EVIDENCE_PACKAGE.md",
  "04_QA_REPORT.md"
)

# ---------- HELPERS ----------

safe_read <- function(path) {
  if (!file.exists(path)) return("")
  x <- tryCatch(
    readLines(path, encoding = "UTF-8", warn = FALSE),
    error = function(e) {
      tryCatch(readLines(path, encoding = "unknown", warn = FALSE),
               error = function(e2) character())
    }
  )
  paste(enc2utf8(x), collapse = "\n")
}

normalize_space <- function(x) {
  x <- ifelse(is.na(x), "", x)
  x <- gsub("[\u2012\u2013\u2014]", "-", x)
  x <- gsub("[[:space:]]+", " ", trimws(x))
  x
}

normalize_title <- function(x) {
  x <- tolower(normalize_space(x))
  x <- gsub("[[:punct:]]+", " ", x)
  gsub("[[:space:]]+", " ", trimws(x))
}

extract_all_pp_ids <- function(text) {
  if (!nzchar(text)) return(character())
  m <- gregexpr("PP-[0-9]{4}", text, perl = TRUE)[[1]]
  if (length(m) == 1L && m[1] == -1L) return(character())
  unique(regmatches(text, list(m))[[1]])
}

# Explicit metadata ID only. We intentionally DO NOT use the first PP-ID
# anywhere in the document, because relationship references are legitimate.
extract_declared_pp_id <- function(text) {
  if (!nzchar(text)) return(NA_character_)
  lines <- strsplit(text, "\n", fixed = TRUE)[[1]]

  patterns <- c(
    "^\\s*\\|?\\s*PP[ _-]*ID\\s*\\|\\s*(PP-[0-9]{4})",
    "^\\s*\\|?\\s*Population Package ID\\s*\\|\\s*(PP-[0-9]{4})",
    "^\\s*\\|?\\s*Package ID\\s*\\|\\s*(PP-[0-9]{4})",
    "^\\s*\\|?\\s*PP Identifier\\s*\\|\\s*(PP-[0-9]{4})"
  )

  for (p in patterns) {
    hit <- grep(p, lines, ignore.case = TRUE, perl = TRUE, value = TRUE)
    if (length(hit)) {
      m <- regexpr("PP-[0-9]{4}", hit[1], perl = TRUE)
      if (m[1] != -1L) return(regmatches(hit[1], m))
    }
  }

  # Common non-table metadata forms.
  p2 <- c(
    "\\bPP[ _-]*ID\\s*[:=]\\s*(PP-[0-9]{4})",
    "\\bPopulation Package ID\\s*[:=]\\s*(PP-[0-9]{4})",
    "\\bPackage ID\\s*[:=]\\s*(PP-[0-9]{4})"
  )
  for (p in p2) {
    m <- regexec(p, text, ignore.case = TRUE, perl = TRUE)
    hit <- regmatches(text, m)[[1]]
    if (length(hit) >= 2L) return(hit[2])
  }

  NA_character_
}

extract_declared_version <- function(text) {
  if (!nzchar(text)) return(NA_character_)
  lines <- strsplit(text, "\n", fixed = TRUE)[[1]]

  fields <- c("Version", "Package Version", "Artifact Version")
  for (field in fields) {
    esc <- gsub("([][{}()+*.^$|?\\\\])", "\\\\\\1", field)
    p <- paste0(
      "^\\s*\\|?\\s*", esc,
      "\\s*\\|\\s*([^|]+)"
    )
    hit <- grep(p, lines, ignore.case = TRUE, perl = TRUE, value = TRUE)
    if (length(hit)) {
      m <- regexpr("[0-9]+\\.[0-9]+\\.[0-9]+", hit[1], perl = TRUE)
      if (m[1] != -1L) return(regmatches(hit[1], m))
    }
  }

  p2 <- "\\b(?:Version|Package Version|Artifact Version)\\s*[:=]\\s*([0-9]+\\.[0-9]+\\.[0-9]+)"
  m <- regexec(p2, text, ignore.case = TRUE, perl = TRUE)
  hit <- regmatches(text, m)[[1]]
  if (length(hit) >= 2L) return(hit[2])

  NA_character_
}

extract_declared_title <- function(text) {
  if (!nzchar(text)) return(NA_character_)
  lines <- strsplit(text, "\n", fixed = TRUE)[[1]]

  fields <- c(
    "Population Package Title",
    "Package Title",
    "Title"
  )

  for (field in fields) {
    esc <- gsub("([][{}()+*.^$|?\\\\])", "\\\\\\1", field)
    p <- paste0(
      "^\\s*\\|?\\s*", esc,
      "\\s*\\|\\s*([^|]+)"
    )
    hit <- grep(p, lines, ignore.case = TRUE, perl = TRUE, value = TRUE)
    if (length(hit)) {
      v <- sub(p, "\\1", hit[1], ignore.case = TRUE, perl = TRUE)
      v <- normalize_space(v)
      if (nzchar(v)) return(v)
    }
  }

  NA_character_
}

heading_names <- function(text) {
  if (!nzchar(text)) return(character())
  lines <- strsplit(text, "\n", fixed = TRUE)[[1]]
  h <- grep("^#{1,6}[[:space:]]+", lines, value = TRUE, perl = TRUE)
  if (!length(h)) return(character())
  h <- sub("^#{1,6}[[:space:]]*", "", h)
  normalize_space(h)
}

has_any <- function(text, patterns) {
  if (!nzchar(text)) return(FALSE)
  any(vapply(patterns, function(p) {
    isTRUE(tryCatch(
      grepl(p, text, ignore.case = TRUE, perl = TRUE),
      error = function(e) FALSE
    ))
  }, logical(1)))
}

count_pattern <- function(text, pattern) {
  if (!nzchar(text)) return(0L)
  m <- tryCatch(
    gregexpr(pattern, text, ignore.case = TRUE, perl = TRUE)[[1]],
    error = function(e) -1L
  )
  if (length(m) == 1L && m[1] == -1L) 0L else length(m)
}

# ---------- SEMANTIC EVIDENCE ----------
# These are deliberately evidence flags, never hard gates.

semantic_flags <- function(texts) {

  CKO <- texts$CKO
  KP  <- texts$KP
  EP  <- texts$EP
  QA  <- texts$QA

  cko_scope <- has_any(CKO, c(
    "scope", "clinical scope", "knowledge scope",
    "intended use", "population boundary"
  ))
  cko_knowledge <- has_any(CKO, c(
    "knowledge block", "clinical knowledge",
    "key message", "knowledge content", "learning objective"
  ))
  cko_graph <- has_any(CKO, c(
    "knowledge graph", "graph position",
    "parent", "upstream", "downstream"
  ))

  kp_governance <- has_any(KP, c(
    "governance", "runtime", "retrieval",
    "version control", "quality status",
    "change history", "update trigger"
  ))
  kp_boundary <- has_any(KP, c(
    "boundary", "explicitly excluded",
    "delegated", "out-of-scope", "out of scope"
  ))

  ep_evidence <- has_any(EP, c(
    "evidence matrix", "evidence table",
    "primary evidence", "supporting evidence",
    "evidence hierarchy", "evidence classification"
  ))
  ep_trace <- has_any(EP, c(
    "traceability", "source traceability",
    "evidence traceability", "reference"
  ))
  ep_boundary <- has_any(EP, c(
    "boundary", "out-of-scope", "out of scope",
    "delegated"
  ))

  qa_content <- has_any(QA, c(
    "content qa", "content quality",
    "content review", "accuracy"
  ))
  qa_clinical <- has_any(QA, c(
    "clinical qa", "clinical quality",
    "clinical review", "clinical"
  ))
  qa_educational <- has_any(QA, c(
    "educational qa", "educational quality",
    "educational review", "education"
  ))
  qa_governance <- has_any(QA, c(
    "governance qa", "governance review",
    "governance", "lifecycle", "retrieval"
  ))
  qa_decision <- has_any(QA, c(
    "final qa decision", "qa decision",
    "final status", "pass", "gold",
    "ready for integration"
  ))

  c(
    CKO_Scope = cko_scope,
    CKO_Knowledge = cko_knowledge,
    CKO_Graph = cko_graph,
    KP_Governance = kp_governance,
    KP_Boundary = kp_boundary,
    EP_Evidence = ep_evidence,
    EP_Traceability = ep_trace,
    EP_Boundary = ep_boundary,
    QA_Content = qa_content,
    QA_Clinical = qa_clinical,
    QA_Educational = qa_educational,
    QA_Governance = qa_governance,
    QA_Decision = qa_decision
  )
}

# ---------- PREFLIGHT ----------

if (!dir.exists(PP_ROOT)) {
  stop(paste0("STOP: Population Package directory not found:\n", PP_ROOT))
}

if (!dir.exists(OUTPUT_DIR)) {
  dir.create(OUTPUT_DIR, recursive = TRUE, showWarnings = FALSE)
}

# ---------- DISCOVER PP FOLDERS ----------

pp_dirs <- list.dirs(PP_ROOT, recursive = FALSE, full.names = TRUE)
pp_dirs <- pp_dirs[basename(pp_dirs) != ""]

folder_id <- function(path) {
  m <- regexec("^(PP-[0-9]{4})(?:\\s|$|[^0-9])", basename(path),
               perl = TRUE)
  hit <- regmatches(basename(path), m)[[1]]
  if (length(hit) >= 2L) hit[2] else NA_character_
}

folder_ids <- vapply(pp_dirs, folder_id, character(1))

# ---------- DUPLICATE FOLDER DETECTION ----------

dup_ids <- unique(folder_ids[duplicated(folder_ids) & !is.na(folder_ids)])

# ---------- AUDIT LOOP ----------

detail_rows <- vector("list", length(EXPECTED_PP_IDS))
depth_rows  <- vector("list", length(EXPECTED_PP_IDS))
semantic_rows <- vector("list", length(EXPECTED_PP_IDS))

for (i in seq_along(EXPECTED_PP_IDS)) {

  pp_id <- EXPECTED_PP_IDS[i]
  idx <- which(folder_ids == pp_id)

  if (!length(idx)) {
    detail_rows[[i]] <- data.frame(
      PP_ID = pp_id,
      Folder_Found = FALSE,
      Duplicate_Folder_ID = FALSE,
      Four_Artifacts = FALSE,
      Canonical_Filenames_OK = FALSE,
      Declared_ID_Status = "HARD_FAIL",
      Declared_Version_Status = "HARD_FAIL",
      Declared_Title_Status = "NOT_AVAILABLE",
      Cross_Artifact_Status = "NOT_APPLICABLE",
      Semantic_Status = "NOT_AVAILABLE",
      Final_v3_Status = "HARD_FAIL",
      Hard_Fail_Reasons = "PP folder not found",
      Cross_Artifact_Findings = "",
      Semantic_Review_Findings = "",
      stringsAsFactors = FALSE
    )
    semantic_rows[[i]] <- data.frame(
      PP_ID = pp_id,
      stringsAsFactors = FALSE
    )
    next
  }

  folder <- pp_dirs[idx[1]]
  duplicate <- length(idx) > 1L

  paths <- file.path(folder, EXPECTED_FILES)
  names(paths) <- c("CKO", "KP", "EP", "QA")
  exists <- file.exists(paths)
  canonical_ok <- all(exists)

  texts <- lapply(paths, safe_read)

  declared_ids <- vapply(texts, extract_declared_pp_id, character(1))
  declared_versions <- vapply(texts, extract_declared_version, character(1))
  declared_titles <- vapply(texts, extract_declared_title, character(1))

  # ID:
  # Missing declaration is NOT a hard failure.
  # Contradiction is a hard failure.
  id_nonmissing <- declared_ids[!is.na(declared_ids) & nzchar(declared_ids)]
  id_contradiction <- length(id_nonmissing) > 0L &&
    any(id_nonmissing != pp_id)

  id_status <- if (id_contradiction) {
    "HARD_FAIL"
  } else if (length(id_nonmissing) == 0L) {
    "NOT_DECLARED"
  } else if (all(id_nonmissing == pp_id)) {
    "PASS"
  } else {
    "REVIEW"
  }

  # Version:
  # Missing declaration is NOT a hard failure.
  # Contradictory explicit versions are hard failure.
  version_nonmissing <- declared_versions[
    !is.na(declared_versions) & nzchar(declared_versions)
  ]
  version_contradiction <- length(version_nonmissing) > 1L &&
    length(unique(version_nonmissing)) > 1L

  version_status <- if (version_contradiction) {
    "HARD_FAIL"
  } else if (length(version_nonmissing) == 0L) {
    "NOT_DECLARED"
  } else if (all(version_nonmissing == "1.0.0")) {
    "PASS"
  } else {
    "REVIEW"
  }

  # Title:
  # Only explicit metadata titles are compared.
  title_nonmissing <- declared_titles[
    !is.na(declared_titles) & nzchar(declared_titles)
  ]
  title_norm <- unique(vapply(title_nonmissing, normalize_title, character(1)))

  title_status <- if (!length(title_nonmissing)) {
    "NOT_DECLARED"
  } else if (length(title_norm) == 1L) {
    "PASS"
  } else {
    "REVIEW"
  }

  cross_findings <- character()

  if (length(id_nonmissing) > 1L && length(unique(id_nonmissing)) > 1L) {
    cross_findings <- c(cross_findings,
                        paste0("Explicit PP ID disagreement: ",
                               paste(unique(id_nonmissing), collapse = " / ")))
  }

  if (length(version_nonmissing) > 1L &&
      length(unique(version_nonmissing)) > 1L) {
    cross_findings <- c(cross_findings,
                        paste0("Explicit version disagreement: ",
                               paste(unique(version_nonmissing), collapse = " / ")))
  }

  if (length(title_norm) > 1L) {
    cross_findings <- c(cross_findings,
                        "Explicit title disagreement across artifacts")
  }

  cross_status <- if (length(cross_findings)) "CROSS_ARTIFACT" else "PASS"

  sem <- semantic_flags(texts)
  sem_count <- sum(sem)

  semantic_findings <- names(sem)[!sem]

  semantic_status <- if (sem_count >= 10L) {
    "EVIDENCE_RICH"
  } else if (sem_count >= 7L) {
    "EVIDENCE_PRESENT"
  } else {
    "SEMANTIC_REVIEW"
  }

  hard_reasons <- character()

  if (!canonical_ok) {
    hard_reasons <- c(
      hard_reasons,
      paste0("Missing canonical artifact(s): ",
             paste(names(exists)[!exists], collapse = ", "))
    )
  }

  if (duplicate) {
    hard_reasons <- c(
      hard_reasons,
      "Duplicate PP folder ID"
    )
  }

  if (id_contradiction) {
    hard_reasons <- c(
      hard_reasons,
      paste0("Explicit PP ID contradicts folder ID: ",
             paste(unique(id_nonmissing[id_nonmissing != pp_id]),
                   collapse = " / "))
    )
  }

  if (version_contradiction) {
    hard_reasons <- c(
      hard_reasons,
      paste0("Explicit version disagreement: ",
             paste(unique(version_nonmissing), collapse = " / "))
    )
  }

  # Cross-artifact disagreement is a true integrity issue only if it
  # concerns explicit identity/version metadata.
  cross_hard <- id_contradiction || version_contradiction

  final_status <- if (length(hard_reasons)) {
    "HARD_FAIL"
  } else if (cross_hard) {
    "HARD_FAIL"
  } else if (length(cross_findings)) {
    "CROSS_ARTIFACT"
  } else {
    "PASS"
  }

  detail_rows[[i]] <- data.frame(
    PP_ID = pp_id,
    Folder_Found = TRUE,
    Duplicate_Folder_ID = duplicate,
    Four_Artifacts = canonical_ok,
    Canonical_Filenames_OK = canonical_ok,
    Declared_ID_Status = id_status,
    Declared_Version_Status = version_status,
    Declared_Title_Status = title_status,
    Cross_Artifact_Status = cross_status,
    Semantic_Status = semantic_status,
    Final_v3_Status = final_status,
    Hard_Fail_Reasons = if (length(hard_reasons))
      paste(hard_reasons, collapse = " | ") else "",
    Cross_Artifact_Findings = if (length(cross_findings))
      paste(cross_findings, collapse = " | ") else "",
    Semantic_Review_Findings = if (length(semantic_findings))
      paste(semantic_findings, collapse = " | ") else "",
    stringsAsFactors = FALSE
  )

  semantic_rows[[i]] <- data.frame(
    PP_ID = pp_id,
    CKO_Scope = sem["CKO_Scope"],
    CKO_Knowledge = sem["CKO_Knowledge"],
    CKO_Graph = sem["CKO_Graph"],
    KP_Governance = sem["KP_Governance"],
    KP_Boundary = sem["KP_Boundary"],
    EP_Evidence = sem["EP_Evidence"],
    EP_Traceability = sem["EP_Traceability"],
    EP_Boundary = sem["EP_Boundary"],
    QA_Content = sem["QA_Content"],
    QA_Clinical = sem["QA_Clinical"],
    QA_Educational = sem["QA_Educational"],
    QA_Governance = sem["QA_Governance"],
    QA_Decision = sem["QA_Decision"],
    Semantic_Evidence_Count = sum(sem),
    stringsAsFactors = FALSE
  )

  depth_rows[[i]] <- data.frame(
    PP_ID = pp_id,
    CKO_Characters = nchar(texts$CKO),
    CKO_Headings = length(heading_names(texts$CKO)),
    CKO_Knowledge_Blocks = count_pattern(
      texts$CKO, "(?m)^#{1,6}\\s+Knowledge Block"
    ),
    KP_Characters = nchar(texts$KP),
    KP_Headings = length(heading_names(texts$KP)),
    EP_Characters = nchar(texts$EP),
    EP_Headings = length(heading_names(texts$EP)),
    EP_Evidence_Matrix_Rows = count_pattern(
      texts$EP, "(?m)^\\s*\\|.*\\|.*\\|"
    ),
    QA_Characters = nchar(texts$QA),
    QA_Headings = length(heading_names(texts$QA)),
    QA_PASS_Mentions = count_pattern(texts$QA, "\\bPASS\\b"),
    stringsAsFactors = FALSE
  )
}

detail <- do.call(rbind, detail_rows)
semantic <- do.call(rbind, semantic_rows)
depth <- do.call(rbind, depth_rows)

# ---------- SUMMARY ----------

hard_fail_n <- sum(detail$Final_v3_Status == "HARD_FAIL")
cross_n <- sum(detail$Final_v3_Status == "CROSS_ARTIFACT")
pass_n <- sum(detail$Final_v3_Status == "PASS")

not_declared_id <- sum(detail$Declared_ID_Status == "NOT_DECLARED")
not_declared_version <- sum(detail$Declared_Version_Status == "NOT_DECLARED")
title_review <- sum(detail$Declared_Title_Status == "REVIEW")

summary <- c(
  "PHASE 3C — LAYER 3 AGGREGATE ARTIFACT AUDIT v3",
  "================================================",
  paste0("Repository root: ", REPO_ROOT),
  paste0("Population Package root: ", PP_ROOT),
  "",
  paste0("Expected PP count: ", length(EXPECTED_PP_IDS)),
  paste0("Audited PP rows: ", nrow(detail)),
  paste0("Complete 4-artifact packages: ", sum(detail$Four_Artifacts), " / 239"),
  paste0("Canonical filename PASS: ", sum(detail$Canonical_Filenames_OK), " / 239"),
  paste0("Duplicate folder IDs: ", sum(detail$Duplicate_Folder_ID), " / 239"),
  "",
  paste0("Explicit ID PASS: ",
         sum(detail$Declared_ID_Status == "PASS"), " / 239"),
  paste0("Explicit ID not declared: ", not_declared_id, " / 239"),
  paste0("Explicit ID hard contradiction: ",
         sum(detail$Declared_ID_Status == "HARD_FAIL"), " / 239"),
  "",
  paste0("Explicit version PASS: ",
         sum(detail$Declared_Version_Status == "PASS"), " / 239"),
  paste0("Explicit version not declared: ",
         not_declared_version, " / 239"),
  paste0("Explicit version hard contradiction: ",
         sum(detail$Declared_Version_Status == "HARD_FAIL"), " / 239"),
  "",
  paste0("Explicit title review: ", title_review, " / 239"),
  "",
  paste0("FINAL PASS: ", pass_n, " / 239"),
  paste0("CROSS_ARTIFACT: ", cross_n, " / 239"),
  paste0("HARD_FAIL: ", hard_fail_n, " / 239"),
  "",
  "SEMANTIC EVIDENCE IS REPORT/REVIEW SIGNAL ONLY.",
  "It is NOT used to fail a package.",
  "",
  "Depth/richness metrics are REPORT ONLY.",
  ""
)

if (hard_fail_n == 0L && cross_n == 0L) {
  summary <- c(
    summary,
    "PROVISIONAL RESULT: OBJECTIVE LAYER 3 INTEGRITY PASS.",
    "Semantic evidence remains available for strategist review."
  )
} else {
  summary <- c(
    summary,
    "PROVISIONAL RESULT: OBJECTIVE INTEGRITY EXCEPTIONS REMAIN."
  )
}

# ---------- OUTPUT ----------

detail_file <- file.path(
  OUTPUT_DIR, "L3_Aggregate_Audit_Detail_v3.csv"
)
semantic_file <- file.path(
  OUTPUT_DIR, "L3_Aggregate_Audit_Semantic_Evidence_v3.csv"
)
depth_file <- file.path(
  OUTPUT_DIR, "L3_Aggregate_Audit_Depth_Metrics_v3.csv"
)
exception_file <- file.path(
  OUTPUT_DIR, "L3_Aggregate_Audit_Exceptions_v3.csv"
)
summary_file <- file.path(
  OUTPUT_DIR, "L3_Aggregate_Audit_Summary_v3.txt"
)

write.csv(detail, detail_file, row.names = FALSE, fileEncoding = "UTF-8")
write.csv(semantic, semantic_file, row.names = FALSE, fileEncoding = "UTF-8")
write.csv(depth, depth_file, row.names = FALSE, fileEncoding = "UTF-8")
write.csv(
  detail[detail$Final_v3_Status != "PASS", ],
  exception_file, row.names = FALSE, fileEncoding = "UTF-8"
)
writeLines(summary, summary_file, useBytes = TRUE)

# ---------- CONSOLE ----------

cat("\n============================================================\n")
cat("LAYER 3 AGGREGATE ARTIFACT AUDIT v3 — COMPLETED\n")
cat("============================================================\n")
cat("Complete 4-artifact packages : ", sum(detail$Four_Artifacts), " / 239\n", sep = "")
cat("Canonical filenames PASS     : ", sum(detail$Canonical_Filenames_OK), " / 239\n", sep = "")
cat("Duplicate folder IDs         : ", sum(detail$Duplicate_Folder_ID), " / 239\n", sep = "")
cat("\n")
cat("Explicit ID PASS             : ",
    sum(detail$Declared_ID_Status == "PASS"), " / 239\n", sep = "")
cat("Explicit ID NOT DECLARED     : ", not_declared_id, " / 239\n", sep = "")
cat("Explicit ID HARD FAIL        : ",
    sum(detail$Declared_ID_Status == "HARD_FAIL"), " / 239\n", sep = "")
cat("\n")
cat("Explicit version PASS        : ",
    sum(detail$Declared_Version_Status == "PASS"), " / 239\n", sep = "")
cat("Explicit version NOT DECLARED: ",
    not_declared_version, " / 239\n", sep = "")
cat("Explicit version HARD FAIL   : ",
    sum(detail$Declared_Version_Status == "HARD_FAIL"), " / 239\n", sep = "")
cat("\n")
cat("FINAL PASS                   : ", pass_n, " / 239\n", sep = "")
cat("CROSS_ARTIFACT              : ", cross_n, " / 239\n", sep = "")
cat("HARD_FAIL                   : ", hard_fail_n, " / 239\n", sep = "")
cat("\nOutput directory:\n", OUTPUT_DIR, "\n", sep = "")
cat("\nFiles created:\n")
cat(" - ", detail_file, "\n", sep = "")
cat(" - ", semantic_file, "\n", sep = "")
cat(" - ", depth_file, "\n", sep = "")
cat(" - ", exception_file, "\n", sep = "")
cat(" - ", summary_file, "\n", sep = "")

if (hard_fail_n == 0L && cross_n == 0L) {
  cat("\nRESULT: PROVISIONAL OBJECTIVE LAYER 3 PASS.\n")
  cat("Semantic evidence remains for strategist review.\n")
} else {
  cat("\nRESULT: OBJECTIVE INTEGRITY EXCEPTIONS REMAIN.\n")
}
