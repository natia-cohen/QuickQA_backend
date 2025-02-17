import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_pymongo import PyMongo
from dotenv import load_dotenv

from api.questions.question_routes import question_bp
from api.answers.answer_routes import answer_bp


load_dotenv()

app = Flask(__name__)
CORS(app) 
socketio = SocketIO(app, cors_allowed_origins="*")

app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/realtime_qa")
mongo = PyMongo(app)

print(mongo.db.list_collection_names())

app.register_blueprint(question_bp)
app.register_blueprint(answer_bp)

if __name__ == "__main__":
    socketio.run(app, debug=True)
