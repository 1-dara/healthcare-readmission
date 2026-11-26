# Capstone: Hospital Readmission Risk Analysis

**Tools:** Python (pandas), PostgreSQL, Tableau Public
**Dataset:** Diabetes 130-US Hospitals (101,766 raw encounters, 99,493 after cleaning)

## The Business Problem
Hospitals are financially penalized when patients are readmitted within 30 days. This project identifies which patient cohorts are at the highest risk, allowing administrators to target post-discharge care.

## Data Cleaning (Python)
- Replaced missing values (`?`) with nulls.
- Dropped sparse columns (`weight`, `max_glu_serum`, `A1Cresult`) that had >80% missing data.
- Filtered out 2,273 rows missing race data.
- Engineered a binary target: `readmitted_30d` (1 = within 30 days, 0 = no).
- Converted age brackets to numeric midpoints for analysis.

## Analysis & SQL (PostgreSQL)
Loaded the cleaned 99,493 rows into PostgreSQL to query high-risk cohorts:
- **Age:** The 20-30 age group had the highest readmission rate (14.40%), contradicting the assumption that older patients are always highest risk.
- **Prior ER Visits:** Readmission risk scales with prior emergency visits (0 visits = 10.5%, 1 visit = 14.4%, 3+ visits = 25.0%).
- **Diagnosis:** Congestive Heart Failure (ICD-9: 428) had the highest readmission rate among top diagnoses (46.5%).

## Dashboard (Tableau)
[Insert your correct Dashboard Link here]

## Recommendation
The hospital should implement a targeted post-discharge follow-up program for:
1. Younger diabetic patients (20–30), who may lack chronic disease management skills.
2. Patients with a history of emergency department visits.
3. Congestive Heart Failure patients, who require strict fluid management protocols.