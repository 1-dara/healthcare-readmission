# MEMORANDUM

**TO:** Hospital Chief Medical Officer / Quality Improvement Committee
**FROM:** Irene, Data Analyst
**DATE:** 26-11-2026
**SUBJECT:** Targeted Strategies to Reduce 30-Day Readmissions

## Executive Summary
Analysis of 99,493 inpatient encounters reveals that the hospital's 30-day readmission rate is **11.2%**. While broad demographic factors like gender do not impact readmission, specific patient cohorts are at significantly higher risk. By targeting post-discharge resources at these specific groups, the hospital can reduce readmissions, improve patient outcomes, and avoid financial penalties.

## Key Findings
1. **The "Younger" Paradox:** Patients aged **20–30** have the highest readmission rate at **14.4%**, followed by the 80–90 group at 12.1%. This suggests younger patients may lack the chronic disease management skills or social support needed to manage diabetes post-discharge.
2. **The ER Red Flag:** Prior emergency department utilization is a massive predictor. Patients with **0 prior ER visits** have a 10.5% readmission rate, but those with **3 or more** prior visits jump to a **25.0%** readmission rate. 
3. **Congestive Heart Failure (CHF):** Among the top primary diagnoses, **ICD-9 code 428 (CHF)** has the highest readmission rate at **46.5%**. Managing fluid balance for CHF patients outside the hospital is highly challenging.

## Strategic Recommendations
1. **Targeted Education for Younger Patients (20–30):** Implement a specialized diabetes education program for younger adults focusing on diet, insulin management, and recognizing early signs of complications.
2. **"Frequent Flyer" Intervention:** Flag any patient with 3+ prior ER visits for an automatic social work consult or case manager assignment before discharge to address underlying social determinants of health.
3. **CHF Discharge Protocol:** For patients diagnosed with CHF (code 428), mandate a follow-up appointment within 7 days and provide a digital scale for daily weight monitoring to catch fluid retention early.

## Methodology
*Data:* Diabetes 130-US Hospitals dataset (101,766 encounters). 
*Cleaning:* Removed columns with >80% missing data (e.g., weight). Converted missing values to nulls. Final sample: 99,493 encounters.
*Tools:* Python (pandas, seaborn), PostgreSQL, Tableau Public.