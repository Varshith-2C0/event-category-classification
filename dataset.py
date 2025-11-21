import pandas as pd
import random

categories = {
    "Technical": [
        "AI workshop", "Python coding bootcamp", "Cloud computing seminar",
        "Hackathon event", "Web development training"
    ],
    "Cultural": [
        "Dance competition", "Music concert", "Art exhibition",
        "Drama night", "Food festival"
    ],
    "Sports": [
        "Cricket tournament", "Football match", "Badminton championship",
        "Marathon run", "Kabaddi league"
    ],
    "Devotional": [
        "Temple festival", "Bhajan session", "Yoga retreat",
        "Spiritual discourse", "Prayer meeting"
    ]
}

data = []

for category, titles in categories.items():
    for i in range(60):  # 240 samples total
        title = random.choice(titles)
        description = f"This event focuses on {title.lower()} and active participation."
        data.append([title, description, category])

df = pd.DataFrame(data, columns=["title", "description", "category"])
df.to_csv("events.csv", index=False)

print("✅ Dataset created: events.csv")
