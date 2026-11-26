import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the cleaned data
df = pd.read_csv('cleaned_diabetic_data.csv')

# Set visual style
sns.set_theme(style="whitegrid")

# --- CHART 1: Time in Hospital vs Readmission ---
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='readmitted_30d', y='time_in_hospital',
            hue='readmitted_30d', palette='Set2', legend=False)
plt.title('Time in Hospital vs 30-Day Readmission', fontsize=14)
plt.xlabel('Readmitted within 30 days (0 = No, 1 = Yes)', fontsize=12)
plt.ylabel('Days in Hospital', fontsize=12)
plt.savefig('time_vs_readmission.png', dpi=300, bbox_inches='tight')
plt.show()

# --- CHART 2: Number of Medications vs Readmission ---
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='readmitted_30d', y='num_medications',
            hue='readmitted_30d', palette='Set2', legend=False)
plt.title('Number of Medications vs 30-Day Readmission', fontsize=14)
plt.xlabel('Readmitted within 30 days (0 = No, 1 = Yes)', fontsize=12)
plt.ylabel('Number of Medications', fontsize=12)
plt.savefig('meds_vs_readmission.png', dpi=300, bbox_inches='tight')
plt.show()

# --- CHART 3: Age vs Readmission Rate (Percentage) ---
# We calculate the readmission rate for each age group
age_readmit = df.groupby('age_numeric')['readmitted_30d'].mean() * 100
plt.figure(figsize=(10, 5))
sns.lineplot(x=age_readmit.index, y=age_readmit.values,
             marker='o', color='crimson')
plt.title('30-Day Readmission Rate by Age Group', fontsize=14)
plt.xlabel('Age (Midpoint of Range)', fontsize=12)
plt.ylabel('Readmission Rate (%)', fontsize=12)
plt.xticks(range(5, 100, 10))  # Set x-ticks every 10 years
plt.savefig('age_vs_readmission.png', dpi=300, bbox_inches='tight')
plt.show()

# --- CHART 4: Primary Diagnosis vs Readmission Rate ---
# Group the top 10 most common diagnoses
top_diag = df['diag_1'].value_counts().head(10).index
diag_readmit = df[df['diag_1'].isin(top_diag)].groupby(
    'diag_1')['readmitted_30d'].mean().sort_values(ascending=False) * 100

plt.figure(figsize=(12, 6))
sns.barplot(x=diag_readmit.values, y=diag_readmit.index,
            hue=diag_readmit.index, palette='viridis', legend=False)
plt.title('30-Day Readmission Rate by Top 10 Primary Diagnoses', fontsize=14)
plt.xlabel('Readmission Rate (%)', fontsize=12)
plt.ylabel('Primary Diagnosis Code', fontsize=12)
plt.savefig('diagnosis_vs_readmission.png', dpi=300, bbox_inches='tight')
plt.show()

print("Charts saved successfully.")

print("\n--- COLUMNS IN CLEANED CSV ---")
print(list(pd.read_csv('cleaned_diabetic_data.csv', nrows=0).columns))
