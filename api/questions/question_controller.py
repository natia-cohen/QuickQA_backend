from flask import Blueprint, request, jsonify
from services.question_service import QuestionService

question_bp = Blueprint("question", __name__)

@question_bp.route("/questions", methods=["POST"])
def add_question():
    data = request.json
    question = QuestionService.add_question(data)
    return jsonify(question), 201

@question_bp.route("/questions", methods=["GET"])
def get_questions():
    return jsonify(QuestionService.get_questions())
