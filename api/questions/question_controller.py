from flask import request, jsonify
from api.questions.question_service import QuestionService

class QuestionController:
    @staticmethod
    def add_question():
        data = request.json
        question = QuestionService.add_question(data)
        return jsonify(question), 201

    @staticmethod
    def get_questions():
        return jsonify(QuestionService.get_questions()), 200
