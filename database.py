from pymongo import MongoClient
from config import Config

try:
    client = MongoClient(Config.MONGO_URI, serverSelectionTimeoutMS=5000)  
    db = client["qa_forum"]


    client.admin.command("ping")
    print("MongoDB Connected Successfully!")

except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    db = None
