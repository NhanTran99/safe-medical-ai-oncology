Đã review **PP-0112 — Circulating Tumor DNA (ctDNA)** dựa trên các source materials của project, đồng thời dùng **Discussion Batch PP-0111** làm template về **format + depth + cách ra quyết định boundary**. PP-0111 đã xác định rất rõ rằng ctDNA phải được tách thành package chuyên biệt tiếp theo, thay vì nhồi toàn bộ ctDNA vào Liquid Biopsy. 

Dưới đây là **Discussion Batch đề xuất cho PP-0112**. Tôi chưa chuyển sang 4-artifact production package; bước này là **scope/design discussion** để khóa architecture trước.

---

# Discussion Batch — PP-0112: Circulating Tumor DNA (ctDNA)

## Following the locked Gold Workflow

### 1. Objective

Xác định **scope atomic** của **PP-0112 — Circulating Tumor DNA (ctDNA)**, nối tiếp:

**PP-0106 Variant Interpretation → PP-0107 Clinical Genomics → PP-0110 Somatic Genetic Testing → PP-0111 Liquid Biopsy**

và mở sang nhánh:

**PP-0112 ctDNA → molecular monitoring / treatment response / tumor evolution / resistance**

Điểm quan trọng nhất:

> **PP-0111 giải thích liquid biopsy như một clinical concept. PP-0112 phải giải thích chính ctDNA: nó là gì, xuất phát từ đâu, có thể cho biết gì, được dùng trong những clinical contexts nào, và giới hạn của nó là gì.**

Discussion PP-0111 đã khóa rõ rằng detailed ctDNA biology, analytics và longitudinal monitoring được delegate sang PP-0112. 

---

# 2. Evidence Discussion — Core Materials

## Consensus chính

Core NCCN Gastric Cancer là nguồn trực tiếp mạnh nhất cho PP-0112.

NCCN mô tả rằng:

* genomic alterations của solid cancers có thể được đánh giá thông qua **ctDNA trong máu**;
* ctDNA xuất phát từ DNA được tumor shed vào circulation;
* phân tích ctDNA có thể phát hiện **mutations, alterations hoặc gene fusions**;
* những findings này có thể giúp nhận diện **targetable alterations**;
* chúng cũng có thể cung cấp thông tin về **evolution of clones with altered treatment-response profiles**;
* trong gastric cancer, blood-based testing có thể được cân nhắc khi **tissue hạn chế** hoặc bệnh nhân advanced/metastatic disease không thể undergo traditional biopsy;
* **negative result không loại trừ sự hiện diện của tumor**. 

Điều này rất phù hợp để xây PP-0112 thành một package **ctDNA-specific**, thay vì chỉ là một repetition của PP-0111.

---

# 3. MUST DECIDE NOW

## Decision 1 — PP-0112 có chỉ cần giải thích “ctDNA là gì” không?

### **Recommendation: NO**

Nếu chỉ định nghĩa ctDNA thì package sẽ quá nông và không tương xứng với vai trò downstream đã được architecture xác định.

PP-0112 nên trả lời đầy đủ chuỗi:

**Tumor**
→ **DNA được giải phóng vào circulation**
→ **ctDNA trong blood**
→ **được thu thập/phân tích**
→ **phát hiện molecular alterations**
→ **clinical interpretation**
→ **possible clinical relevance**
→ **possible longitudinal use**

Nhưng phải dừng trước:

* detailed sequencing;
* variant classification;
* treatment algorithm.

---

# 4. MUST DECIDE NOW — ctDNA có phải là toàn bộ liquid biopsy không?

### **Recommendation: NO — MUST PRESERVE**

Đây là boundary đã được PP-0111 LOCK.

**Liquid biopsy** là khái niệm rộng hơn.

**ctDNA** là một dạng/ứng dụng genomic quan trọng của liquid biopsy.

Vì vậy:

### PP-0111

> **What is Liquid Biopsy?**

### PP-0112

> **What is ctDNA and what can ctDNA tell us?**

Không được đảo ngược hierarchy.

Discussion PP-0111 đã explicitly reject phương án biến PP-0111 thành ctDNA package và xác định PP-0112 là package chuyên biệt downstream. 

---

# 5. MUST DECIDE NOW — Có bao gồm biology của ctDNA không?

### **Recommendation: YES — foundational / conceptual**

Đây là điểm PP-0112 cần sâu hơn PP-0111.

Người học cần hiểu:

* ctDNA là gì;
* ctDNA đến từ đâu;
* tumor cells có thể giải phóng DNA vào bloodstream;
* ctDNA là một phần của circulating cell-free DNA;
* lượng ctDNA có thể thay đổi theo tumor burden, biology và clinical context.

Nhưng:

❌ Không đi vào detailed molecular biology của DNA fragmentation.

❌ Không đi vào nucleosome footprints.

❌ Không đi vào technical cfDNA extraction.

❌ Không đi vào sequencing chemistry.

Mục tiêu là:

> **Hiểu nguồn gốc và ý nghĩa của ctDNA, không phải trở thành một molecular-biology/NGS textbook.**

---

# 6. MUST DECIDE NOW — Có bao gồm ctDNA khác với cfDNA như thế nào không?

### **Recommendation: YES — important**

Đây là một distinction rất hữu ích và nên có trong PP-0112.

### Conceptual hierarchy

**Cell-free DNA (cfDNA)**
= DNA fragments tự do trong circulation.

**ctDNA**
= phần cfDNA có nguồn gốc từ tumor.

Do đó:

> **ctDNA ⊂ cfDNA**

Điều này giúp bệnh nhân hiểu vì sao xét nghiệm máu không đơn giản là “đọc toàn bộ DNA của tumor”.

### Boundary

Chỉ giải thích ở mức conceptual.

Không biến package thành “cfDNA biology”.

---

# 7. MUST DECIDE NOW — Có bao gồm “tumor fraction / lượng ctDNA” không?

### **Recommendation: YES — conceptual**

Đây là một limitation quan trọng.

Không phải mọi bệnh nhân đều có cùng lượng ctDNA trong máu.

Một mẫu blood có thể chứa:

* nhiều cfDNA không phải tumor;
* một lượng nhỏ ctDNA;
* hoặc trong một số trường hợp rất ít/khó phát hiện ctDNA.

Do đó:

> **Không phát hiện ctDNA hoặc không phát hiện một alteration không đồng nghĩa chắc chắn alteration đó không tồn tại trong tumor.**

Điều này phải nối trực tiếp với warning của NCCN rằng negative liquid-biopsy result không loại trừ tumor. 

Không đưa numeric thresholds nếu Core Materials không cung cấp.

---

# 8. MUST DECIDE NOW — Có bao gồm “ctDNA có thể phát hiện gì?” không?

### **Recommendation: YES — core**

Đây phải là một trong những knowledge blocks trung tâm.

Theo NCCN, ctDNA analysis trong gastric cancer có thể phát hiện:

* mutations;
* genomic alterations;
* gene fusions. 

Có thể giải thích ở mức patient-facing:

> ctDNA có thể cung cấp thông tin về những thay đổi di truyền/molecular changes của tumor đang lưu hành trong máu.

Không cần lập danh sách dài từng loại genomic alteration.

---

# 9. MUST DECIDE NOW — Có bao gồm targetable alterations?

### **Recommendation: YES — conceptual**

Đây là evidence-supported clinical relevance.

NCCN ghi nhận rằng detection of mutations/alterations/fusions từ DNA shed by gastric carcinomas có thể giúp identify **targetable alterations**. 

Nhưng boundary phải rất rõ:

### Được

**ctDNA**
→ genomic alteration
→ potentially clinically relevant / potentially targetable

### Không được

**ctDNA**
→ mutation X
→ drug Y chắc chắn phù hợp.

Treatment selection vẫn thuộc downstream precision-treatment packages.

---

# 10. MUST DECIDE NOW — Có bao gồm tumor evolution không?

### **Recommendation: YES — CORE**

Đây có lẽ là clinical concept quan trọng nhất để PP-0112 khác biệt với PP-0111.

NCCN trực tiếp nói rằng genomic alterations detected from DNA shed from gastric carcinomas có thể giúp nhận diện:

> **evolution of clones with altered treatment response profiles.** 

Do đó PP-0112 nên giải thích:

**Tumor evolves over time**

→ different tumor clones may emerge/change

→ molecular profile can change

→ ctDNA may provide a blood-based window into some of those molecular changes.

Đây là nền tảng để hiểu:

* treatment resistance;
* molecular progression;
* changing tumor biology.

---

# 11. MUST DECIDE NOW — Có bao gồm treatment resistance không?

### **Recommendation: YES — conceptual, not algorithmic**

NCCN đã support **altered treatment-response profiles**. 

Vì vậy có thể introduce:

> ctDNA có thể cung cấp thông tin về những molecular changes liên quan đến sự thay đổi response của tumor đối với treatment.

Nhưng không nên dạy:

> “ctDNA tăng = chắc chắn kháng thuốc.”

Hoặc:

> “ctDNA mutation X = đổi sang treatment Y.”

Đó là interpretation + clinical decision-making.

---

# 12. MUST DECIDE NOW — Có bao gồm treatment-response monitoring?

### **Recommendation: YES — nhưng cần phân tầng evidence rất rõ**

Đây là điểm tôi đề nghị **không viết quá mạnh**.

PP-0112 nên giới thiệu rằng ctDNA có tiềm năng/được nghiên cứu và sử dụng trong một số context để theo dõi **molecular changes over time**, nhưng không nên biến thành claim rằng:

> ctDNA là standard universal replacement for imaging or clinical assessment.

Core NCCN hiện support tumor molecular evolution và treatment-response relevance, nhưng không đủ để biến PP-0112 thành một universal ctDNA monitoring guideline. 

### Recommended wording architecture

**ctDNA can provide dynamic molecular information over time.**

↓

**Changes in ctDNA may provide information about changes in tumor biology.**

↓

**The clinical meaning depends on the disease, assay and clinical context.**

↓

**ctDNA does not automatically replace imaging, pathology or clinical assessment.**

---

# 13. MUST DECIDE NOW — Có bao gồm minimal residual disease (MRD)?

### **Recommendation: LIMITED / DEFER as a major topic**

Tôi **không recommend đưa MRD thành một major knowledge block của PP-0112** nếu Core Materials hiện tại không có đủ authoritative gastric-cancer evidence để support it.

Có thể mention conceptually ở mức:

> ctDNA đang được nghiên cứu/sử dụng trong một số cancer settings để tìm molecular evidence of residual disease.

Nhưng:

❌ không xây thành “ctDNA-MRD package”.

❌ không đưa cut-off.

❌ không đưa postoperative surveillance algorithm.

Nếu project sau này có dedicated **Molecular Residual Disease / ctDNA Monitoring PP**, nội dung này nên delegate sang đó.

---

# 14. MUST DECIDE NOW — Có bao gồm recurrence surveillance?

### **Recommendation: DEFER / NOT CORE**

Không nên để PP-0112 trở thành:

> “ctDNA test to detect recurrence.”

Lý do:

* đây là một **specific clinical application**;
* cần disease-stage-specific evidence;
* cần distinction giữa molecular detection và clinically actionable recurrence;
* dễ overlap future surveillance/MRD packages.

PP-0112 chỉ cần nói rằng:

> ctDNA can potentially provide longitudinal molecular information.

Detailed recurrence surveillance → downstream.

---

# 15. MUST DECIDE NOW — Có bao gồm diagnosis?

### **Recommendation: NO as primary purpose**

Không được xây:

> “ctDNA diagnoses gastric cancer.”

PP-0111 đã xác định liquid biopsy không nên được trình bày như replacement for tissue diagnosis. 

PP-0112 phải giữ nguyên principle:

> **ctDNA provides molecular information; it does not automatically replace tissue diagnosis.**

---

# 16. MUST DECIDE NOW — Có bao gồm tissue vs ctDNA comparison không?

### **Recommendation: YES — core but concise**

Đây là một trong những nội dung patient-facing hữu ích nhất.

| Tissue-based testing                   | ctDNA                                                                       |
| -------------------------------------- | --------------------------------------------------------------------------- |
| Directly samples tumor tissue          | Uses tumor-derived DNA circulating in blood                                 |
| Gives tissue/pathologic context        | Gives blood-based molecular information                                     |
| May require biopsy                     | Usually blood-based                                                         |
| May be limited by tissue availability  | May be useful when tissue is limited                                        |
| Represents sampled tissue at that time | Can potentially provide information from circulating tumor-derived material |
| May be invasive                        | Less invasive sampling                                                      |

Nhưng không được diễn đạt rằng ctDNA **luôn superior**.

### Key message

> **ctDNA complements tissue-based evaluation; it does not universally replace it.**

---

# 17. MUST DECIDE NOW — Có bao gồm technical workflow?

### **Recommendation: NO**

Explicitly exclude:

* blood collection tubes;
* plasma separation protocol;
* cfDNA extraction protocol;
* library preparation;
* sequencing chemistry;
* digital PCR technical workflow;
* NGS variant-calling pipeline;
* bioinformatic filtering;
* analytical validation;
* limit-of-detection calculations.

Những nội dung này thuộc:

**NGS / Molecular Testing / technical ctDNA package**, không phải patient-facing PP-0112.

---

# 18. MUST DECIDE NOW — Có bao gồm CTC không?

### **Recommendation: NO**

CTC = circulating tumor cells.

Dù CTC có liên quan đến liquid biopsy, PP-0111 đã cố tình không mở rộng sang CTC vì Core Materials đang tập trung vào blood-based ctDNA. 

Do đó:

**PP-0112 = ctDNA**

Không:

**PP-0112 = all circulating tumor components.**

---

# 19. MUST DECIDE NOW — Có bao gồm cfDNA như một package riêng không?

### **Recommendation: NO**

Chỉ cần:

**cfDNA → ctDNA relationship**

để giải thích nguồn gốc.

Không đi sâu vào:

* cfDNA biology;
* non-tumor cfDNA;
* cfDNA fragmentation;
* cfDNA kinetics.

---

# 20. MUST DECIDE NOW — Có bao gồm serial / longitudinal sampling?

### **Recommendation: YES — conceptual**

Đây là cầu nối tự nhiên tới clinical monitoring.

Người học cần hiểu:

> ctDNA có thể được đo tại các thời điểm khác nhau.

Ví dụ conceptually:

**baseline**
→ **during treatment**
→ **later time point**

Điều này cho phép nhìn vào **change over time**, thay vì chỉ một molecular snapshot.

Nhưng:

❌ không quy định lịch lấy máu;

❌ không quy định tuần thứ mấy;

❌ không đặt threshold response;

❌ không đưa algorithm.

---

# 21. MUST DECIDE NOW — Có bao gồm ctDNA dynamics?

### **Recommendation: YES — conceptual**

Đây là nội dung nên được nhấn mạnh hơn PP-0111.

Một result duy nhất:

> **What molecular alterations are detectable now?**

Serial results:

> **How is the molecular profile changing over time?**

Đây là lý do ctDNA có giá trị đặc biệt trong **dynamic tumor assessment**.

Tuy nhiên, phải nhấn mạnh:

> **A change in ctDNA is information that requires clinical interpretation; it is not by itself a treatment decision.**

---

# 22. MUST DECIDE NOW — Có bao gồm “ctDNA positive/negative” như binary result không?

### **Recommendation: YES, but explain carefully**

Không nên dạy:

* ctDNA positive = active cancer;
* ctDNA negative = no cancer.

Thay vào đó:

### Positive

Có thể cho thấy tumor-derived molecular material đang được phát hiện.

### Negative

Có nghĩa là **không phát hiện được ctDNA/alteration bằng assay trong mẫu đó**.

Nó không tự động chứng minh:

* không còn tumor;
* không còn disease;
* không có genomic alteration.

NCCN trực tiếp cảnh báo rằng negative liquid-biopsy result không loại trừ tumor. 

---

# 23. MUST DECIDE NOW — Có cần nói về “ctDNA không phải tumor DNA nguyên vẹn” không?

### **Recommendation: YES — very briefly**

Đây là một conceptual clarification tốt:

> ctDNA thường tồn tại dưới dạng DNA fragments trong circulation, không phải một mẫu tumor nguyên vẹn.

Điều này giúp người đọc hiểu tại sao:

* blood test không cho morphology;
* blood test không thay thế pathology;
* amount of tumor-derived DNA có thể thấp.

Nhưng không đi vào detailed DNA fragmentation biology.

---

# 24. Trade-Off

## Option A — PP-0112 = “Definition of ctDNA”

❌ **REJECT**

Quá nông.

Không tận dụng clinical relevance của ctDNA.

---

## Option B — PP-0112 = “Complete ctDNA laboratory/NGS technology”

❌ **REJECT**

Overlap:

* NGS;
* molecular testing;
* technical laboratory packages.

Không phù hợp patient-facing atomic PP.

---

## Option C — PP-0112 = “All applications of liquid biopsy”

❌ **REJECT**

Overlap PP-0111.

---

## Option D — **ctDNA as a clinical molecular biomarker**

### **RECOMMEND**

Architecture:

**Tumor**
→ **DNA released into blood**
→ **ctDNA**
→ **molecular alterations**
→ **interpretation**
→ **clinical relevance**
→ **tumor evolution**
→ **potential response/resistance information**
→ **longitudinal molecular information**
→ **limitations**

Đây là architecture cân bằng nhất.

---

# 25. RECOMMENDED SCOPE — PP-0112

## Primary Educational Question

> **What is circulating tumor DNA (ctDNA), and what can it tell us about gastric cancer?**

Tôi recommend câu này hơn:

> “How is ctDNA used to monitor gastric cancer?”

vì monitoring chỉ là **một application**, không phải toàn bộ package.

---

# 26. Included

PP-0112 nên bao gồm:

1. Definition of ctDNA.
2. Relationship between ctDNA and cfDNA.
3. Where ctDNA comes from.
4. How ctDNA reaches the bloodstream.
5. Why ctDNA can provide molecular information about a tumor.
6. What ctDNA can detect:

   * mutations;
   * genomic alterations;
   * gene fusions.
7. ctDNA versus tissue-based testing.
8. When blood-based ctDNA testing may be useful.
9. Limited tissue / inability to undergo traditional biopsy.
10. Identification of potentially targetable alterations.
11. Tumor molecular heterogeneity/evolution at conceptual level.
12. Treatment-response profile changes.
13. Potential relevance to resistance.
14. Longitudinal/dynamic ctDNA information.
15. Conceptual treatment-response monitoring.
16. Limitations and false-negative/undetected findings.
17. Why negative ctDNA does not prove absence of tumor.
18. Why ctDNA does not automatically determine treatment.
19. Patient-facing interpretation.
20. Common misconceptions.

---

# 27. Explicitly Excluded

* detailed NGS methodology;
* digital PCR methodology;
* cfDNA extraction;
* plasma processing;
* library preparation;
* sequencing chemistry;
* bioinformatics;
* variant calling;
* variant interpretation;
* variant classification;
* ACMG/ClinGen criteria;
* detailed MRD algorithms;
* recurrence-surveillance algorithms;
* treatment-switch algorithms;
* CTC;
* exosomes;
* other liquid-biopsy analytes;
* disease-specific ctDNA cut-offs;
* numerical sensitivity/specificity thresholds;
* individualized ctDNA interpretation.

---

# 28. Proposed Knowledge Architecture

### Knowledge Block 1

**What Is Circulating Tumor DNA (ctDNA)?**

---

### Knowledge Block 2

**Where Does ctDNA Come From?**

---

### Knowledge Block 3

**How Is ctDNA Related to Cell-Free DNA (cfDNA)?**

---

### Knowledge Block 4

**What Can ctDNA Tell Us About a Tumor?**

---

### Knowledge Block 5

**What Genomic Changes Can ctDNA Detect?**

---

### Knowledge Block 6

**Why Might ctDNA Be Useful When Tissue Is Limited?**

---

### Knowledge Block 7

**How Is ctDNA Different From Tissue-Based Testing?**

---

### Knowledge Block 8

**Can ctDNA Identify Potentially Targetable Alterations?**

---

### Knowledge Block 9

**Can ctDNA Show That a Tumor Is Changing?**

---

### Knowledge Block 10

**Can ctDNA Provide Information About Treatment Response or Resistance?**

---

### Knowledge Block 11

**Why Can ctDNA Be Measured Over Time?**

---

### Knowledge Block 12

**What Does a Positive or Negative ctDNA Result Mean?**

---

### Knowledge Block 13

**What Are the Limitations of ctDNA Testing?**

---

### Knowledge Block 14

**Does ctDNA Replace Tissue Biopsy or Imaging?**

---

# 29. Common Misconceptions

### Myth 1

**“ctDNA and liquid biopsy are exactly the same thing.”**

**Fact:**
ctDNA is a major genomic application of liquid biopsy; liquid biopsy is the broader concept. PP-0111 covers the broader concept, while PP-0112 focuses specifically on ctDNA. 

---

### Myth 2

**“A negative ctDNA test means there is no cancer.”**

**Fact:**
A negative result does not exclude the presence of a tumor. 

---

### Myth 3

**“ctDNA replaces a tissue biopsy.”**

**Fact:**
ctDNA provides blood-based molecular information and may be particularly useful when tissue is limited, but it does not universally replace tissue diagnosis or pathology. 

---

### Myth 4

**“If ctDNA finds a mutation, that mutation definitely explains the whole cancer.”**

**Fact:**
ctDNA provides molecular information about tumor-derived DNA. Its significance requires appropriate interpretation and clinical context.

---

### Myth 5

**“ctDNA tells the doctor which drug to prescribe.”**

**Fact:**
ctDNA may identify potentially targetable alterations, but treatment decisions require additional evidence and clinical context. 

---

### Myth 6

**“ctDNA always detects every mutation in the tumor.”**

**Fact:**
The amount of tumor-derived DNA in blood can be limited, and a blood-based assay may not detect every alteration present in the tumor.

---

### Myth 7

**“If ctDNA changes, the treatment definitely failed.”**

**Fact:**
Changes in ctDNA can provide molecular information about tumor biology, but they do not automatically establish treatment failure without appropriate clinical interpretation.

---

### Myth 8

**“ctDNA is only useful after treatment.”**

**Fact:**
ctDNA can provide molecular information at different points in the clinical course, including when tissue is limited and when tumor molecular evolution is being assessed.

---

# 30. Evidence-Supported Clinical Use Model

A useful architecture for the final PP is:

### Use 1 — Molecular characterization

**What genomic alterations are detectable in the tumor-derived DNA?**

↓

### Use 2 — Potential treatment relevance

**Is there an alteration that may be clinically relevant or potentially targetable?**

↓

### Use 3 — Tumor evolution

**Has the molecular profile changed over time?**

↓

### Use 4 — Treatment-response context

**Does the molecular information provide evidence about changing treatment-response profiles?**

↓

### Use 5 — Longitudinal molecular monitoring

**How is the ctDNA profile changing across time points?**

This should be presented as a **conceptual clinical-use ladder**, not as a universal treatment algorithm.

The first three levels are particularly well anchored in the gastric-cancer NCCN material. 

---

# 31. Knowledge Graph Decision

## Prerequisites

* **PP-0107 — Clinical Genomics**
* **PP-0110 — Somatic Genetic Testing**
* **PP-0111 — Liquid Biopsy**
* Molecular testing / NGS fundamentals

---

## Related

* PP-0106 — Variant Interpretation
* NGS
* Gene Panel Testing
* Molecular Tumor Profiling
* Biomarker Testing
* Precision Oncology
* Treatment Response
* Resistance

---

## Downstream

Potential future packages:

**PP-0112 ctDNA**
→ **Molecular Monitoring**
→ **ctDNA Response Monitoring**
→ **ctDNA / MRD**
→ **Molecular Recurrence Detection**

if and when these are separately defined.

---

# 32. Critical Boundary With PP-0111

| PP-0111 — Liquid Biopsy         | PP-0112 — ctDNA                    |
| ------------------------------- | ---------------------------------- |
| What is liquid biopsy?          | What is ctDNA?                     |
| Broad clinical concept          | Specific molecular analyte         |
| Blood/plasma application        | Biology/source of ctDNA            |
| Why liquid biopsy may be useful | What ctDNA can detect              |
| Tissue vs liquid concept        | ctDNA vs tissue                    |
| Limited tissue                  | ctDNA-specific limitations         |
| ctDNA introduced                | ctDNA explained in depth           |
| Tumor evolution introduced      | ctDNA dynamics/evolution explained |
| No detailed monitoring          | Conceptual longitudinal use        |
| No detailed ctDNA biology       | Foundational ctDNA biology         |

PP-0111 explicitly delegates detailed ctDNA and longitudinal monitoring to PP-0112. 

---

# 33. Critical Boundary With PP-0106

### PP-0106 — Variant Interpretation

**What does a detected genomic variant mean?**

### PP-0112 — ctDNA

**What tumor-derived DNA can be detected in blood, and what clinical information can that provide?**

Therefore PP-0112 may say:

> “The detected alteration requires interpretation.”

But it must **not teach the interpretation/classification framework again**.

---

# 34. Critical Boundary With PP-0110

### PP-0110 — Somatic Genetic Testing

**How is somatic genetic testing performed conceptually and why is it used?**

### PP-0112 — ctDNA

**How can blood-derived tumor DNA serve as a source of somatic molecular information?**

PP-0112 therefore represents a **specimen/source-specific extension of somatic molecular testing**, not a replacement for PP-0110.

The PP-0110 discussion already explicitly excluded liquid biopsy/ctDNA methodology and placed PP-0111/PP-0112 downstream. 

---

# 35. Evidence Hierarchy Proposal

## Level I — Direct gastric-cancer guideline evidence

### NCCN Gastric Cancer

Strongest direct source for PP-0112.

Supports:

* ctDNA in blood;
* genomic alterations;
* mutations/alterations/fusions;
* potentially targetable alterations;
* tumor-clone evolution;
* advanced/metastatic gastric cancer;
* limited tissue;
* inability to undergo traditional biopsy;
* negative-result limitation. 

---

## Level I — Oncology education framework

### ESMO/ASCO Global Curriculum

Use for:

* molecular oncology;
* genomic testing;
* clinical interpretation;
* treatment monitoring/resistance concepts;
* integration into oncology workflow. 

---

## Supporting evidence

* peer-reviewed ctDNA reviews;
* gastric-cancer ctDNA studies;
* validated molecular-monitoring literature.

Nhưng những sources này chỉ được dùng để **expand** the educational synthesis, không để vượt quá governance scope.

---

# 36. Important Evidence Boundary

Có một điểm cần giữ rất chặt:

NCCN hiện support **clinical utility of ctDNA-based genomic testing in selected gastric-cancer contexts**, nhưng điều đó **không đồng nghĩa rằng mọi possible ctDNA application đều đã là routine standard of care**.

Do đó trong final CKO/Evidence Package nên phân biệt:

### Established / guideline-supported

* ctDNA as a blood-based source of tumor genomic information;
* detection of genomic alterations;
* selected use when tissue is limited/unavailable;
* potential identification of targetable alterations;
* molecular information about tumor evolution.

### Emerging / context-dependent

* serial response monitoring;
* resistance monitoring;
* MRD;
* recurrence detection;
* treatment-change decisions based primarily on ctDNA dynamics.

Đây là một distinction tôi **khuyến nghị bắt buộc** trong PP-0112 để tránh overclaim.

---

# 37. Final Scope Recommendation

## **PP-0112 — LOCK PROPOSAL**

> **Approve PP-0112 as a specialized, patient-facing Population Package answering “What is circulating tumor DNA (ctDNA), and what can it tell us about gastric cancer?”, covering the biological concept and origin of ctDNA, its relationship to cfDNA, detection of tumor-derived genomic alterations, potential clinical relevance including targetable alterations and tumor evolution, the role of longitudinal molecular information, selected treatment-response/resistance concepts, and key limitations including false-negative/undetected findings.**

> **Explicitly exclude detailed NGS/assay methodology, variant interpretation/classification, CTC and other liquid-biopsy analytes, detailed MRD/recurrence algorithms, numerical ctDNA thresholds, treatment-switch algorithms, and individualized ctDNA interpretation.**

### Overall recommendation

# **LOCK PP-0112 with this scope.**

**No architecture blocker identified.**

The architecture is clean:

**PP-0110 Somatic Genetic Testing**
↓
**PP-0111 Liquid Biopsy**
↓

# **PP-0112 ctDNA**

↓
**future specialized molecular monitoring / MRD / resistance applications**

This also preserves the exact hierarchy already established in the PP-0111 Discussion: **Somatic Genetic Testing → Liquid Biopsy → ctDNA → specialized clinical applications.** 

**Nếu lock scope này, bước kế tiếp sẽ là production của full 4-artifact Gold package cho PP-0112 theo đúng depth của PP-0106/PP trước đó.**
