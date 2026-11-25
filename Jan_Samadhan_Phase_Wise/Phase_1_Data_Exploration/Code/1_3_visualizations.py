"""Task 1.3: Visualize top departments and complaint trends over time."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "jan_samadhan_sample_500.csv")
df["Date"] = pd.to_datetime(df["Date"])

top5 = df["Department"].value_counts().head(5)
ax = top5.sort_values().plot(kind="barh", figsize=(8, 5), title="Top 5 Departments by Complaint Volume")
ax.set_xlabel("Number of complaints")
ax.set_ylabel("Department")
plt.tight_layout()
plt.savefig(ROOT / "outputs" / "plots" / "top_5_departments.png", dpi=150)
plt.close()

monthly = df.set_index("Date").resample("MS").size()
ax = monthly.plot(figsize=(9, 5), marker="o", title="Monthly Complaint Volume Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Number of complaints")
plt.tight_layout()
plt.savefig(ROOT / "outputs" / "plots" / "monthly_complaint_trend.png", dpi=150)
plt.close()

print("Top 5 departments:\n", top5.to_string())
print("\nMonthly complaint counts:\n", monthly.to_string())
print("\nCharts saved in outputs/plots/")
