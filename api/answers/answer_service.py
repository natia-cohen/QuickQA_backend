from bson import ObjectId
from database import db
class AnswerService:
    @staticmethod
    def add_answer(question_id, answer_text):
        try:
            question = db["questions"].find_one({"_id": ObjectId(question_id)})

            if not question:
                return False  

            db["questions"].update_one(
                {"_id": ObjectId(question_id)},
                {"$push": {"answers": answer_text}}
            )

    
            return True
        except Exception as e:
            return False



