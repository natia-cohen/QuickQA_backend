from flask import Blueprint
from api.questions.question_controller import QuestionController

question_bp = Blueprint("question", __name__)


question_bp.route("/questions", methods=["POST"])(QuestionController.add_question)
question_bp.route("/questions", methods=["GET"])(QuestionController.get_questions)
