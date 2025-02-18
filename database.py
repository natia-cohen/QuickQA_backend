import json
from pymongo import MongoClient
from config import Config

try:
    client = MongoClient(Config.MONGO_URI, serverSelectionTimeoutMS=5000)  
    db = client["qa_forum"]
    client.admin.command("ping")
    print("MongoDB Connected Successfully!")

except Exception as e:
    print(f" Error connecting to MongoDB: {e}")
    db = None  

def seed_database():
    if db is not None:

        collection = db["questions"]

        try:
            with open("questions.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                if data:
                    collection.insert_many(data)
                    print(" Database seeded successfully!")
                else:
                    print("No data found in questions.json")
        except Exception as e:
            print(f"Error inserting data: {e}")

if __name__ == "__main__":
    seed_database()
