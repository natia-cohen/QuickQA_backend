from flask import request, jsonify
from flask_socketio import emit
from api.answers.answer_service import AnswerService

class AnswerController:
    @staticmethod
    def add_answer():
        data = request.json
        success = AnswerService.add_answer(data["question_title"], data["answer"])
        if success:
            emit("new_answer", data["answer"], broadcast=True)  
            return jsonify({"message": "Answer added successfully"}), 201
        return jsonify({"error": "Question not found"}), 404

    @staticmethod
    def get_answers():
        question_title = request.args.get("question_title")
        answers = AnswerService.get_answers(question_title)
        if answers is not None:
            return jsonify({"answers": answers}), 200
        return jsonify({"error": "Question not found"}), 404
