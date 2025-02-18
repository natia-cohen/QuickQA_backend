from database import db
from datetime import datetime

class QuestionService:
    @staticmethod
    def add_question(data):
        question = {
            "title": data["title"],
            "content": data["content"],
            "created_at": datetime.utcnow().isoformat(),  
            "user_id": data.get("user_id", "anonymous"),  
            "answers": [] 
        }
        inserted_question = db["questions"].insert_one(question)
        question["_id"] = str(inserted_question.inserted_id)
        return question

    @staticmethod
    def get_questions():
        questions = list(db["questions"].find({}, {"_id": 1, "title": 1, "content": 1, "created_at": 1, "user_id": 1, "answers": 1}))

        for question in questions:
            question["_id"] = str(question["_id"]) 
            if "answers" in question and isinstance(question["answers"], list):
                for answer in question["answers"]:
                    if isinstance(answer, dict) and "id" in answer:
                        answer["id"] = str(answer["id"])  

        return questions
