"""Task 2.2: Evaluate the classifier with accuracy and confusion matrix."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay

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
pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, pred):.3f}")
print("\nClassification report:\n", classification_report(y_test, pred, zero_division=0))
disp = ConfusionMatrixDisplay.from_predictions(y_test, pred, xticks_rotation=35, cmap="Blues")
disp.figure_.set_size_inches(9, 7)
plt.tight_layout()
plt.savefig(ROOT / "outputs" / "plots" / "confusion_matrix.png", dpi=150)
plt.close()
print("Confusion matrix chart saved to outputs/plots/confusion_matrix.png")
