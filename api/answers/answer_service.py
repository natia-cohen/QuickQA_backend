from database import db
from bson import ObjectId  

class AnswerService:
    @staticmethod
    def add_answer(question_id, answer):
        try:
            object_id = ObjectId(question_id)  
        except:
            return False 

        question = db["questions"].find_one({"_id": object_id})
        if question:
            db["questions"].update_one(
                {"_id": object_id},
                {"$push": {"answers": answer}}
            )
            return True
        return False

    @staticmethod
    def get_answers(question_id):
   
        try:
            object_id = ObjectId(question_id)
        except:
            return None  

        question = db["questions"].find_one({"_id": object_id})
        if question:
            return question.get("answers", [])
        return None
