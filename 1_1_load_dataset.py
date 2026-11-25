"""Task 1.1: Load the Jan-Samadhan dataset and identify structured/unstructured fields."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "jan_samadhan_sample_500.csv")
structured = ["Complaint_ID", "State", "Date", "Department", "Status", "Resolution_Days"]
unstructured = ["Complaint_Description"]

print("Dataset shape:", df.shape)
print("\nStructured columns:", structured)
print("Unstructured columns:", unstructured)
print("\nData types:\n", df.dtypes)
print("\nFirst five records:\n", df.head().to_string(index=False))
