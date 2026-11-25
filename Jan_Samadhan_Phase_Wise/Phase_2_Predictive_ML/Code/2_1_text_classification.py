"""Task 2.1: Train a supervised text classifier to route complaints."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "jan_samadhan_sample_500.csv").dropna(subset=["Complaint_Description", "Department"])
X_train, X_test, y_train, y_test = train_test_split(
    df["Complaint_Description"], df["Department"], test_size=0.2,
    random_state=42, stratify=df["Department"]
)
model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", ngram_range=(1, 2), max_features=3000)),
    ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
])
model.fit(X_train, y_train)
(ROOT / "outputs").mkdir(exist_ok=True)
joblib.dump(model, ROOT / "outputs" / "department_router.joblib")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
sample = ["My electricity bill is incorrect and power supply is interrupted."]
print("Sample complaint:", sample[0])
print("Predicted department:", model.predict(sample)[0])
print("Model saved to outputs/department_router.joblib")
