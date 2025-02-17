from database import db

class QuestionService:
    @staticmethod
    def add_question(data):
        question = {
            "title": data["title"],
            "content": data["content"],
            "answers": []
        }
        inserted_question = db["questions"].insert_one(question) 
        question["_id"] = str(inserted_question.inserted_id)  
        return question

    @staticmethod
    def get_questions():
        questions = list(db["questions"].find({}, {"_id": 1, "title": 1, "content": 1}))  
        for question in questions:
            question["_id"] = str(question["_id"])  
        return questions
