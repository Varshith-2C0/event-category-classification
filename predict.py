import joblib

model = joblib.load("event_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

text = input("Enter event description: ")
text_vec = vectorizer.transform([text])

prediction = model.predict(text_vec)
print("🔹 Predicted Category:", prediction[0])
