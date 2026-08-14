# ============================================================
# PHASE 3C — LAYER 3 AGGREGATE ARTIFACT AUDIT v2
# CALIBRATED / LOW-FALSE-POSITIVE VERSION
#
# Purpose:
#   Aggregate verification of PP-0001 -> PP-0239
#   without treating exact heading wording as a hard failure.
#
# IMPORTANT:
#   - READ-ONLY. Does not modify Gold Markdown or Git.
#   - Base R only.
#   - Run from / against the repository root.
#   - Depth/richness metrics are REPORT ONLY.
#   - Clinical accuracy remains governed by approved QA.
#
# Classification:
#   HARD_PASS / HARD_FAIL
#   REVIEW
#   REPORT_ONLY
#
# Principle:
#   Do NOT "fix" packages because v1.4 rejected a heading name.
#   Hard failures are reserved for identity/completeness/version/
#   canonical-file failures. Semantic/structural evidence is
#   calibrated with aliases and otherwise sent to REVIEW.
# ============================================================

options(stringsAsFactors = FALSE, warn = 1)

# ---------- 1. CONFIGURATION ----------

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
EXPECTED_VERSION <- "1.0.0"

# ---------- 2. HELPERS ----------

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

safe_bool <- function(x) isTRUE(x)

has_text <- function(text, pattern) {
  if (length(text) != 1L || is.na(text) || !nzchar(text)) return(FALSE)
  isTRUE(tryCatch(
    grepl(pattern, text, ignore.case = TRUE, perl = TRUE),
    error = function(e) FALSE
  ))
}

has_any_text <- function(text, patterns) {
  any(vapply(patterns, function(p) has_text(text, p), logical(1)))
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

normalize_text <- function(x) {
  x <- ifelse(is.na(x), "", x)
  x <- gsub("[\u2012\u2013\u2014]", "-", x)
  x <- gsub("[[:space:]]+", " ", trimws(x))
  tolower(x)
}

normalize_title <- function(x) {
  x <- normalize_text(x)
  x <- gsub("[[:punct:]]+", " ", x)
  gsub("[[:space:]]+", " ", trimws(x))
}

heading_names <- function(text) {
  if (length(text) != 1L || is.na(text) || !nzchar(text)) return(character())
  lines <- strsplit(text, "\n", fixed = TRUE)[[1]]
  h <- grep("^#{1,6}[[:space:]]+", lines, value = TRUE, perl = TRUE)
  if (!length(h)) return(character())
  h <- sub("^#{1,6}[[:space:]]*", "", h)
  h <- gsub("[[:space:]]+", " ", trimws(h))
  unique(h)
}

heading_any <- function(text, aliases) {
  h <- tolower(heading_names(text))
  if (!length(h)) return(FALSE)
  any(vapply(
    aliases,
    function(a) any(grepl(tolower(a), h, fixed = TRUE)),
    logical(1)
  ))
}

# Flexible metadata extraction: accepts table rows and common variants.
extract_field <- function(text, fields) {
  if (length(text) != 1L || is.na(text) || !nzchar(text)) return(NA_character_)
  lines <- strsplit(text, "\n", fixed = TRUE)[[1]]
  for (field in fields) {
    f <- gsub("([][{}()+*.^$|\\?\\\\])", "\\\\\\1", field)
    p <- paste0(
      "^\\s*(?:\\|\\s*)?", f,
      "\\s*(?:\\||:)", "\\s*(.*?)\\s*(?:\\|\\s*)?$"
    )
    hit <- grep(p, lines, ignore.case = TRUE, perl = TRUE, value = TRUE)
    if (length(hit)) {
      v <- sub(p, "\\1", hit[1], ignore.case = TRUE, perl = TRUE)
      v <- trimws(v)
      if (nzchar(v)) return(v)
    }
  }
  NA_character_
}

extract_pp_identity <- function(text) {
  fields <- c(
    "PP ID", "Population Package ID", "Package ID",
    "Population Package", "PP Identifier"
  )
  v <- extract_field(text, fields)
  if (!is.na(v)) {
    m <- regexpr("PP-[0-9]{4}", v, perl = TRUE)
    if (m[1] != -1L) return(regmatches(v, m))
  }
  NA_character_
}

extract_version <- function(text) {
  v <- extract_field(text, c("Version", "Package Version", "Artifact Version"))
  if (is.na(v)) return(NA_character_)
  m <- regexpr("[0-9]+\\.[0-9]+\\.[0-9]+", v, perl = TRUE)
  if (m[1] == -1L) return(NA_character_)
  regmatches(v, m)
}

extract_title <- function(text) {
  v <- extract_field(text, c(
    "Title", "Population Package Title", "Package Title",
    "Knowledge Title"
  ))
  if (!is.na(v)) return(v)

  h <- heading_names(text)
  if (!length(h)) return(NA_character_)

  # Prefer an explicit title-like heading, not generic headings.
  idx <- grep("^(?:PP-[0-9]{4}\\s*[-:|]|Population Package|Clinical Knowledge Object|Knowledge Passport|Primary Evidence Package|QA Report)",
              h, ignore.case = TRUE, perl = TRUE)
  if (length(idx)) return(h[idx[1]])
  NA_character_
}

required_aliases <- list(
  CKO = list(
    metadata = c("Metadata", "Document Metadata", "Package Metadata"),
    objectives = c("Educational Objectives", "Learning Objectives", "Objectives"),
    scope = c("Scope", "Clinical Scope", "Knowledge Scope"),
    blocks = c("Clinical Knowledge Blocks", "Knowledge Blocks", "Knowledge Block"),
    messages = c("Key Messages", "Key Message", "Core Messages"),
    graph = c("Knowledge Graph", "Knowledge Graph Position", "Graph"),
    history = c("Revision History", "Change History", "Version History")
  ),
  KP = list(
    identity = c("Identity", "Package Identity", "Population Package Identity"),
    classification = c("Knowledge Classification", "Classification"),
    journey = c("Patient Journey Classification", "Patient Journey"),
    runtime = c("Primary Runtime Role", "Runtime Role", "Primary Runtime"),
    secondary = c("Secondary Runtime Roles", "Secondary Runtime Role", "Runtime Roles"),
    triggers = c("Typical Trigger Questions", "Trigger Questions", "Typical Questions"),
    retrieval = c("Retrieval Priority", "Retrieval"),
    graph = c("Knowledge Graph", "Knowledge Graph Position", "Graph"),
    scope = c("Clinical Scope", "Scope"),
    excluded = c("Explicitly Excluded", "Explicit Exclusions", "Excluded"),
    sources = c("Authoritative Sources", "Authoritative Source"),
    evidence = c("Evidence Classification", "Evidence"),
    boundary = c("Intended Knowledge Boundaries", "Knowledge Boundaries", "Boundaries"),
    governance = c("Governance Metadata", "Governance"),
    version = c("Version Control", "Version"),
    history = c("Change History", "Revision History"),
    triggers2 = c("Future Update Triggers", "Update Triggers", "Future Updates"),
    quality = c("Quality Status", "Quality"),
    final = c("Final Status", "Final QA Status", "Status")
  ),
  EP = list(
    identity = c("Identity", "Package Identity"),
    question = c("Clinical Question", "Clinical Questions"),
    intent = c("Educational Intent", "Educational Purpose", "Intent"),
    scope = c("Scope", "Clinical Scope"),
    primary = c("Primary Evidence Sources", "Primary Evidence", "Primary Sources"),
    supporting = c("Supporting Sources", "Supporting Evidence"),
    hierarchy = c("Evidence Hierarchy", "Evidence Level", "Evidence Classification"),
    matrix = c("Evidence Matrix", "Evidence Table", "Evidence Summary Matrix"),
    claims = c("Clinical Claims Summary", "Claims Summary", "Clinical Claims"),
    gaps = c("Evidence Gaps", "Evidence Limitations", "Gaps"),
    excluded = c("Out-of-Scope Topics", "Out-of-Scope Topics / Delegated Packages",
                 "Out of Scope", "Explicitly Excluded"),
    updates = c("Future Update Triggers", "Update Triggers", "Future Updates"),
    trace = c("Source Traceability", "Evidence Traceability", "Traceability"),
    boundary = c("Boundary Verification", "Boundary", "Scope Boundary"),
    final = c("Final Evidence Status", "Evidence Status", "Final Status")
  ),
  QA = list(
    identity = c("Identity", "Package Identity"),
    objective = c("QA Objective", "Quality Assurance Objective", "Audit Objective"),
    content = c("Layer 1 — Content QA", "Layer 1 - Content QA", "Content QA", "Content Quality"),
    clinical = c("Layer 2 — Clinical QA", "Layer 2 - Clinical QA", "Clinical QA", "Clinical Quality"),
    educational = c("Layer 3 — Educational QA", "Layer 3 - Educational QA", "Educational QA"),
    governance = c("Layer 4 — Governance QA", "Layer 4 - Governance QA", "Governance QA"),
    cross = c("Cross-Artifact Consistency Check", "Cross Artifact Consistency",
              "Cross-Artifact Check", "Cross Artifact Check"),
    decision = c("Final QA Decision", "QA Decision", "Final Decision"),
    final = c("Final Status", "Final QA Status", "Status")
  )
)

artifact_structure <- function(text, artifact) {
  a <- required_aliases[[artifact]]
  present <- vapply(a, function(x) heading_any(text, x), logical(1))
  # Structure is a calibrated evidence signal, not an automatic hard failure.
  list(
    pass = sum(present) >= ceiling(length(present) * 0.75),
    strong = sum(present) >= ceiling(length(present) * 0.90),
    present = present,
    missing = names(present)[!present]
  )
}

boundary_check <- function(kp, ep, qa) {
  kp_core <- has_any_text(kp, c("\\bCore\\b"))
  kp_support <- has_any_text(kp, c("\\bSupporting\\b", "Supporting Knowledge"))
  kp_excluded <- has_any_text(kp, c("Explicitly Excluded", "Explicit Exclusions", "Excluded"))
  kp_delegated <- has_any_text(kp, c("Delegated-to PP", "Delegated to PP", "Delegated"))
  ep_boundary <- heading_any(ep, required_aliases$EP$boundary) ||
    has_any_text(ep, c("Boundary Verification", "Explicitly Excluded", "Delegated"))
  qa_boundary <- has_any_text(qa, c("Boundary Completeness", "Boundary Verification", "Boundary"))

  core <- kp_core && kp_support && kp_excluded && kp_delegated
  any_evidence <- core || ep_boundary || qa_boundary

  c(
    hard = FALSE,
    pass = any_evidence,
    strong = core && ep_boundary
  )
}

evidence_check <- function(ep) {
  matrix_ok <- heading_any(ep, required_aliases$EP$matrix) ||
    has_any_text(ep, c("Evidence Matrix", "Evidence Table"))
  trace_ok <- heading_any(ep, required_aliases$EP$trace) ||
    has_any_text(ep, c("Source Traceability", "Evidence Traceability", "Traceability"))
  primary_ok <- heading_any(ep, required_aliases$EP$primary) ||
    has_any_text(ep, c("Primary Evidence Sources", "Primary Evidence"))
  hierarchy_ok <- heading_any(ep, required_aliases$EP$hierarchy) ||
    has_any_text(ep, c("Evidence Hierarchy", "Evidence Level", "Evidence Classification"))

  strong <- matrix_ok && trace_ok && primary_ok
  pass <- sum(c(matrix_ok, trace_ok, primary_ok, hierarchy_ok)) >= 3
  c(pass = pass, strong = strong)
}

qa_status_check <- function(qa) {
  # Accept governed punctuation/wording variants.
  p1 <- has_text(qa, "\\bPASS\\b")
  p2 <- has_text(qa, "\\bGOLD\\b")
  p3 <- has_text(qa, "READY\\s+FOR\\s+INTEGRATION")
  final_heading <- heading_any(qa, required_aliases$QA$final)
  strong <- p1 && p2 && p3 && final_heading
  pass <- p1 && p2 && p3
  c(pass = pass, strong = strong)
}

cross_artifact_check <- function(pp_id, texts, ids, versions) {
  ids_ok <- all(!is.na(ids) & ids == pp_id)
  versions_ok <- all(!is.na(versions) & versions == EXPECTED_VERSION)
  qa_cross <- heading_any(texts$QA, required_aliases$QA$cross) ||
    has_any_text(texts$QA, c("cross-artifact", "cross artifact", "artifact consistency"))
  strong <- ids_ok && versions_ok && qa_cross
  pass <- ids_ok && versions_ok
  c(pass = pass, strong = strong, qa_cross = qa_cross)
}

# ---------- 3. PREFLIGHT ----------

if (!dir.exists(PP_ROOT)) {
  stop(paste0("STOP: Population Package directory not found:\n", PP_ROOT))
}
if (!dir.exists(OUTPUT_DIR)) {
  dir.create(OUTPUT_DIR, recursive = TRUE, showWarnings = FALSE)
}

# ---------- 4. DISCOVER FOLDERS BY ACTUAL BASENAME ----------

pp_dirs <- list.dirs(PP_ROOT, recursive = FALSE, full.names = TRUE)
pp_dirs <- pp_dirs[basename(pp_dirs) != ""]

extract_folder_id <- function(x) {
  m <- regexpr("^PP-[0-9]{4}(?:\\s|$|[^0-9])", basename(x), perl = TRUE)
  if (m[1] == -1L) return(NA_character_)
  sub("^((?:PP-[0-9]{4})).*$", "\\1", basename(x), perl = TRUE)
}

folder_ids <- vapply(pp_dirs, extract_folder_id, character(1))

# ---------- 5. AUDIT ----------

rows <- vector("list", length(EXPECTED_PP_IDS))
depth_rows <- vector("list", length(EXPECTED_PP_IDS))

for (i in seq_along(EXPECTED_PP_IDS)) {
  pp_id <- EXPECTED_PP_IDS[i]
  matches <- which(folder_ids == pp_id)

  if (!length(matches)) {
    rows[[i]] <- data.frame(
      PP_ID = pp_id, Folder_Found = FALSE, Four_Artifacts = FALSE,
      Canonical_Filenames_OK = FALSE, ID_Hard_OK = FALSE, Version_Hard_OK = FALSE,
      Title_Hard_OK = NA, Structure_Status = "REVIEW",
      Boundary_Status = "REVIEW", Evidence_Status = "REVIEW",
      QA_Status = "REVIEW", Cross_Artifact_Status = "REVIEW",
      Aggregate_v2_Status = "HARD_FAIL",
      Hard_Fail_Reasons = "PP folder not found",
      Review_Reasons = "", stringsAsFactors = FALSE
    )
    next
  }

  folder <- pp_dirs[matches[1]]
  files <- file.path(folder, EXPECTED_FILES)
  names(files) <- c("CKO", "KP", "EP", "QA")
  exists <- file.exists(files)
  texts <- lapply(files, safe_read)

  canonical_ok <- all(exists)

  ids <- vapply(texts, extract_pp_identity, character(1))
  versions <- vapply(texts, extract_version, character(1))
  titles <- vapply(texts, extract_title, character(1))

  id_hard <- canonical_ok && all(!is.na(ids) & ids == pp_id)
  version_hard <- canonical_ok && all(!is.na(versions) & versions == EXPECTED_VERSION)

  title_norm <- vapply(titles, normalize_title, character(1))
  title_known <- all(nzchar(title_norm))
  title_consistent <- title_known && length(unique(title_norm)) == 1L

  # Title is not a hard fail when wording differs; it is REVIEW.
  title_hard <- if (title_consistent) TRUE else NA

  structures <- lapply(names(texts), function(a) {
    artifact_structure(texts[[a]], a)
  })
  names(structures) <- names(texts)

  structure_pass_count <- sum(vapply(structures, function(x) x$pass, logical(1)))
  structure_strong_count <- sum(vapply(structures, function(x) x$strong, logical(1)))

  structure_status <- if (structure_strong_count == 4L) {
    "HARD_PASS"
  } else if (structure_pass_count == 4L) {
    "PASS_WITH_VARIANTS"
  } else {
    "REVIEW"
  }

  b <- boundary_check(texts$KP, texts$EP, texts$QA)
  boundary_status <- if (b["strong"]) "HARD_PASS" else if (b["pass"]) "PASS_WITH_VARIANTS" else "REVIEW"

  e <- evidence_check(texts$EP)
  evidence_status <- if (e["strong"]) "HARD_PASS" else if (e["pass"]) "PASS_WITH_VARIANTS" else "REVIEW"

  q <- qa_status_check(texts$QA)
  qa_status <- if (q["strong"]) "HARD_PASS" else if (q["pass"]) "PASS_WITH_VARIANTS" else "REVIEW"

  c <- cross_artifact_check(pp_id, texts, ids, versions)
  cross_status <- if (c["strong"]) "HARD_PASS" else if (c["pass"]) "PASS_WITH_VARIANTS" else "REVIEW"

  hard_reasons <- character()
  review_reasons <- character()

  if (!canonical_ok) {
    hard_reasons <- c(hard_reasons, paste("Missing canonical artifact(s):",
                                          paste(names(exists)[!exists], collapse = ", ")))
  }
  if (!id_hard) {
    hard_reasons <- c(hard_reasons, "Artifact identity field missing/mismatched")
  }
  if (!version_hard) {
    hard_reasons <- c(hard_reasons, "Version missing/mismatched (expected 1.0.0)")
  }

  if (is.na(title_hard) || !title_hard) {
    review_reasons <- c(review_reasons, "Title evidence is missing or differs across artifacts")
  }
  if (structure_status == "REVIEW") {
    review_reasons <- c(review_reasons, "One or more artifact structures need semantic review")
  }
  if (boundary_status == "REVIEW") {
    review_reasons <- c(review_reasons, "Boundary evidence needs review")
  }
  if (evidence_status == "REVIEW") {
    review_reasons <- c(review_reasons, "Evidence/traceability evidence needs review")
  }
  if (qa_status == "REVIEW") {
    review_reasons <- c(review_reasons, "QA final-status evidence needs review")
  }
  if (cross_status == "REVIEW") {
    review_reasons <- c(review_reasons, "Cross-artifact consistency evidence needs review")
  }

  # IMPORTANT:
  # Semantic/structural uncertainty is REVIEW, not automatic HARD_FAIL.
  final_status <- if (length(hard_reasons)) {
    "HARD_FAIL"
  } else if (length(review_reasons)) {
    "REVIEW"
  } else {
    "PASS"
  }

  rows[[i]] <- data.frame(
    PP_ID = pp_id,
    Folder_Found = TRUE,
    Four_Artifacts = canonical_ok,
    Canonical_Filenames_OK = canonical_ok,
    ID_Hard_OK = id_hard,
    Version_Hard_OK = version_hard,
    Title_Hard_OK = title_hard,
    Structure_Status = structure_status,
    Boundary_Status = boundary_status,
    Evidence_Status = evidence_status,
    QA_Status = qa_status,
    Cross_Artifact_Status = cross_status,
    Aggregate_v2_Status = final_status,
    Hard_Fail_Reasons = if (length(hard_reasons)) paste(hard_reasons, collapse = " | ") else "",
    Review_Reasons = if (length(review_reasons)) paste(review_reasons, collapse = " | ") else "",
    stringsAsFactors = FALSE
  )

  depth_rows[[i]] <- data.frame(
    PP_ID = pp_id,
    CKO_Characters = nchar(texts$CKO),
    CKO_Headings = length(heading_names(texts$CKO)),
    CKO_Knowledge_Blocks = count_pattern(texts$CKO, "(?m)^#{1,6}\\s+Knowledge Block"),
    KP_Characters = nchar(texts$KP),
    KP_Headings = length(heading_names(texts$KP)),
    EP_Characters = nchar(texts$EP),
    EP_Headings = length(heading_names(texts$EP)),
    EP_Evidence_Matrix_Rows = if (heading_any(texts$EP, required_aliases$EP$matrix)) 1L else 0L,
    QA_Characters = nchar(texts$QA),
    QA_Headings = length(heading_names(texts$QA)),
    QA_PASS_Mentions = count_pattern(texts$QA, "\\bPASS\\b"),
    stringsAsFactors = FALSE
  )
}

detail <- do.call(rbind, rows)
depth <- do.call(rbind, depth_rows)

# ---------- 6. SUMMARY ----------

hard_fail_n <- sum(detail$Aggregate_v2_Status == "HARD_FAIL")
review_n <- sum(detail$Aggregate_v2_Status == "REVIEW")
pass_n <- sum(detail$Aggregate_v2_Status == "PASS")

summary_lines <- c(
  "PHASE 3C — LAYER 3 AGGREGATE ARTIFACT AUDIT v2 — CALIBRATED",
  "============================================================",
  paste0("Repository root: ", REPO_ROOT),
  paste0("Population Package root: ", PP_ROOT),
  "",
  paste0("Expected PP count: ", length(EXPECTED_PP_IDS)),
  paste0("Audited PP rows: ", nrow(detail)),
  paste0("Complete 4-artifact packages: ", sum(detail$Four_Artifacts), " / 239"),
  paste0("Canonical filename PASS: ", sum(detail$Canonical_Filenames_OK), " / 239"),
  paste0("Hard identity PASS: ", sum(detail$ID_Hard_OK), " / 239"),
  paste0("Hard version PASS: ", sum(detail$Version_Hard_OK), " / 239"),
  paste0("Structure strong PASS: ", sum(detail$Structure_Status == "HARD_PASS"), " / 239"),
  paste0("Boundary strong PASS: ", sum(detail$Boundary_Status == "HARD_PASS"), " / 239"),
  paste0("Evidence strong PASS: ", sum(detail$Evidence_Status == "HARD_PASS"), " / 239"),
  paste0("QA strong PASS: ", sum(detail$QA_Status == "HARD_PASS"), " / 239"),
  paste0("Cross-artifact strong PASS: ", sum(detail$Cross_Artifact_Status == "HARD_PASS"), " / 239"),
  "",
  paste0("FINAL v2 STATUS — PASS: ", pass_n, " / 239"),
  paste0("FINAL v2 STATUS — REVIEW: ", review_n, " / 239"),
  paste0("FINAL v2 STATUS — HARD_FAIL: ", hard_fail_n, " / 239"),
  "",
  "Interpretation:",
  "- HARD_FAIL is reserved for missing packages/artifacts or hard identity/version failures.",
  "- REVIEW means evidence exists but semantic wording/structure requires strategist review.",
  "- PASS means no hard failures and no unresolved review signals.",
  "- Depth/richness metrics are REPORT ONLY and are never used as a quality gate.",
  ""
)

if (hard_fail_n == 0L && review_n == 0L) {
  summary_lines <- c(
    summary_lines,
    "PROVISIONAL RESULT: 239/239 PASS — READY FOR STRATEGIST FINAL REVIEW."
  )
} else if (hard_fail_n == 0L) {
  summary_lines <- c(
    summary_lines,
    "PROVISIONAL RESULT: NO HARD FAILURES. REVIEW CLASSIFICATION REMAINS BEFORE LAYER 3 PASS."
  )
} else {
  summary_lines <- c(
    summary_lines,
    "PROVISIONAL RESULT: HARD FAILURES REQUIRE REVIEW."
  )
}

# ---------- 7. WRITE OUTPUTS ----------

detail_file <- file.path(OUTPUT_DIR, "L3_Aggregate_Audit_Detail_v2.csv")
depth_file <- file.path(OUTPUT_DIR, "L3_Aggregate_Audit_Depth_Metrics_v2.csv")
exception_file <- file.path(OUTPUT_DIR, "L3_Aggregate_Audit_Exceptions_v2.csv")
summary_file <- file.path(OUTPUT_DIR, "L3_Aggregate_Audit_Summary_v2.txt")

write.csv(detail, detail_file, row.names = FALSE, fileEncoding = "UTF-8")
write.csv(depth, depth_file, row.names = FALSE, fileEncoding = "UTF-8")
exceptions <- detail[detail$Aggregate_v2_Status != "PASS", ]
write.csv(exceptions, exception_file, row.names = FALSE, fileEncoding = "UTF-8")
writeLines(summary_lines, summary_file, useBytes = TRUE)

# ---------- 8. CONSOLE ----------

cat("\n============================================================\n")
cat("LAYER 3 AGGREGATE ARTIFACT AUDIT v2 — COMPLETED\n")
cat("============================================================\n")
cat("Complete 4-artifact packages: ", sum(detail$Four_Artifacts), " / 239\n", sep = "")
cat("Hard identity PASS:           ", sum(detail$ID_Hard_OK), " / 239\n", sep = "")
cat("Hard version PASS:            ", sum(detail$Version_Hard_OK), " / 239\n", sep = "")
cat("Structure strong PASS:        ", sum(detail$Structure_Status == "HARD_PASS"), " / 239\n", sep = "")
cat("Boundary strong PASS:         ", sum(detail$Boundary_Status == "HARD_PASS"), " / 239\n", sep = "")
cat("Evidence strong PASS:         ", sum(detail$Evidence_Status == "HARD_PASS"), " / 239\n", sep = "")
cat("QA strong PASS:               ", sum(detail$QA_Status == "HARD_PASS"), " / 239\n", sep = "")
cat("Cross-artifact strong PASS:   ", sum(detail$Cross_Artifact_Status == "HARD_PASS"), " / 239\n", sep = "")
cat("\nFINAL PASS:       ", pass_n, " / 239\n", sep = "")
cat("FINAL REVIEW:     ", review_n, " / 239\n", sep = "")
cat("FINAL HARD_FAIL:  ", hard_fail_n, " / 239\n", sep = "")
cat("\nOutput directory:\n", OUTPUT_DIR, "\n\n", sep = "")
if (hard_fail_n == 0L && review_n == 0L) {
  cat("RESULT: PROVISIONAL PASS — 239/239\n")
  cat("Strategist final review remains required before Layer 3 is declared PASS.\n")
} else if (hard_fail_n == 0L) {
  cat("RESULT: NO HARD FAILURES — REVIEW ITEMS REMAIN.\n")
} else {
  cat("RESULT: HARD FAILURES DETECTED — REVIEW REQUIRED.\n")
}
cat("\nFiles created:\n")
cat(" - ", detail_file, "\n", sep = "")
cat(" - ", depth_file, "\n", sep = "")
cat(" - ", exception_file, "\n", sep = "")
cat(" - ", summary_file, "\n", sep = "")
