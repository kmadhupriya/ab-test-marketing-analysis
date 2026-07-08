import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Data load pannu
df = pd.read_csv('marketing_AB.csv')

# First rows paaru, columns enna nu
print(df.head())
print()
print(df.columns.tolist())
# 1. Ella group um enna count nu paaru
print("GROUP SIZES:")
print(df['test group'].value_counts())
print()

# 2. Conversion rate by group
print("CONVERSION RATE BY GROUP:")
conversion_rate = df.groupby('test group')['converted'].mean()
print(conversion_rate)
print()

# 3. Statistical significance test (Chi-square test)
from scipy.stats import chi2_contingency

# Contingency table create pannu
contingency_table = pd.crosstab(df['test group'], df['converted'])
print("CONTINGENCY TABLE:")
print(contingency_table)
print()

chi2, p_value, dof, expected = chi2_contingency(contingency_table)
print(f"Chi-square statistic: {chi2:.4f}")
print(f"P-value: {p_value:.10f}")

if p_value < 0.05:
    print("RESULT: Statistically significant difference (p < 0.05) — Ad group performs differently than PSA group, this is NOT due to random chance.")
else:
    print("RESULT: No statistically significant difference (p >= 0.05) — difference could be due to random chance.")
    

conversion_rate.plot(kind='bar', title='Conversion Rate: Ad vs PSA Group', color=['orange', 'gray'])
plt.ylabel('Conversion Rate')
plt.tight_layout()
plt.savefig('ab_test_conversion.png')
print("Chart saved as ab_test_conversion.png")
