from flask import Blueprint
from api.answers.answer_controller import AnswerController

answer_bp = Blueprint("answer", __name__)

answer_bp.route("/answer", methods=["POST"])(AnswerController.add_answer)
answer_bp.route("/answers", methods=["GET"])(AnswerController.get_answers)
