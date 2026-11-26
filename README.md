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

## Interactive Dashboard (Tableau)
You can view the visual analysis of these risk factors here:
https://public.tableau.com/app/profile/irene.peter.okon/viz/HospitalReadmissionRiskFactors/Dashboard1#1

## Business Recommendation
A full memorandum detailing the strategic recommendations for the hospital is included in this repository: [Read the Memo](memo.md).

**Summary of Recommendations:**
1. Implement targeted education for younger patients (20-30) who may lack chronic disease management skills.
2. Flag patients with 3+ prior ER visits for an automatic social work consult.
3. Mandate a 7-day follow-up and daily weight monitoring for Congestive Heart Failure patients.

## Repository Contents
- `explore_data.py`: Python script for data inspection, cleaning, and feature engineering.
- `eda_healthcare.py`: Python script for generating the exploratory visualizations.
- `memo.md`: The executive recommendation memo.
- `data_age.csv`, `data_emergency.csv`, `data_diagnoses.csv`: Aggregated data used for the Tableau dashboard.