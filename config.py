import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/qa_forum")
    

    SOCKETIO_CORS_ALLOWED_ORIGINS = "*"


    DEBUG = True

