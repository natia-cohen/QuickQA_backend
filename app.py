from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from api.questions.question_routes import question_bp
from api.answers.answer_routes import answer_bp

app = Flask(__name__)
CORS(app) 
socketio = SocketIO(app, cors_allowed_origins="*")


app.register_blueprint(question_bp)
app.register_blueprint(answer_bp)

if __name__ == "__main__":
    socketio.run(app, debug=True)
