"""Task 1.2: Handle missing values and clean complaint text."""
from pathlib import Path
import re
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "data" / "jan_samadhan_sample_500.csv"
out = ROOT / "outputs" / "cleaned_complaints.csv"

df = pd.read_csv(source)
df["State"] = df["State"].fillna("Unknown")
df["Complaint_Description"] = df["Complaint_Description"].fillna("")
def clean_text(value):
    value = str(value)
    value = re.sub(r"[^A-Za-z0-9\s.,!?'-]", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value
df["Complaint_Description"] = df["Complaint_Description"].apply(clean_text)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Resolution_Days"] = pd.to_numeric(df["Resolution_Days"], errors="coerce")
df["Resolution_Days"] = df["Resolution_Days"].fillna(df["Resolution_Days"].median())
df.to_csv(out, index=False)
print("Missing values after cleaning:\n", df.isna().sum().to_string())
print(f"\nCleaned dataset saved to: {out}")
print("\nExample cleaned complaint:\n", df.loc[0, "Complaint_Description"])
