from flask import request, jsonify
from flask_socketio import emit
from api.answers.answer_service import AnswerService

class AnswerController:
    @staticmethod
    def add_answer():
        data = request.json
        question_id = data.get("question_id") 
        answer_text = data.get("answer")

        if not question_id or not answer_text:
            return jsonify({"error": "Missing question_id or answer"}), 400

        success = AnswerService.add_answer(question_id, answer_text)
        if success:
            # emit("new_answer", answer_text, broadcast=True)  
            return jsonify({"message": "Answer added successfully"}), 201
        return jsonify({"error": "Question not found"}), 404

    @staticmethod
    def get_answers():
        question_id = request.args.get("question_id") 
        answers = AnswerService.get_answers(question_id)
        
        if answers is not None:
            return jsonify({"answers": answers}), 200
        return jsonify({"error": "Question not found"}), 404
