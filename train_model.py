import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import joblib

# Load data
df = pd.read_csv("events.csv")

# Preprocessing
df["text"] = df["title"] + " " + df["description"]

# Vectorization
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["text"])
y = df["category"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = metrics.accuracy_score(y_test, y_pred)
f1 = metrics.f1_score(y_test, y_pred, average="weighted")

print("✅ Accuracy:", accuracy)
print("✅ F1 Score:", f1)

# Save model
joblib.dump(model, "event_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model saved")
