from bson import ObjectId
from datetime import datetime
from database import db

class AnswerService:
    @staticmethod
    def add_answer(question_id, answer_text, user_id):
        try:
            question = db["questions"].find_one({"_id": ObjectId(question_id)})

            if not question:
                return False  

            new_answer = {
                "id": str(ObjectId()),
                "text": answer_text,
                "user_id": user_id,
                "created_at": datetime.utcnow().isoformat()
            }

            db["questions"].update_one(
                {"_id": ObjectId(question_id)},
                {"$push": {"answers": new_answer}}
            )

            return new_answer
        except Exception as e:
            return False

    @staticmethod
    def get_answers(question_id):
        try:
            question = db["questions"].find_one({"_id": ObjectId(question_id)}, {"answers": 1})

            if not question:
                return None

            return question["answers"]
        except Exception as e:
            return None
