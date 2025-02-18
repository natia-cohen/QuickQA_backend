# QuickQA - Backend (Flask + MongoDB)

##  Overview
This is the backend for QuickQA, a real-time Q&A application where users can post questions and answers.

---

##  Installation & Setup
###  **Clone the Repository**
Run the following commands:
```sh
 git clone <repository-url>
 cd QuickQA/backend
```

###  **Backend Setup (Flask + MongoDB)**
#### ** Prerequisites**
- Python 3.8+
- MongoDB installed and running
- Flask and dependencies installed

####  **Steps to Run Backend**
1. **Navigate to the backend directory**:
```sh
 cd backend
```
2. **Create & activate a virtual environment** (optional but recommended):
```sh
 python -m venv venv
 source venv/bin/activate  # macOS/Linux
 venv\Scripts\activate  # Windows
```
3. **Install dependencies**:
```sh
 pip install -r requirements.txt
```
4. **Start the Flask server**:
```sh
 python app.py
```
5. The API will now be running at:
```
 http://127.0.0.1:5000
```

---

## 🌐 API Endpoints
### Questions API:
- **GET** `/questions` → Retrieve all questions
- **POST** `/questions` → Create a new question

### Answers API:
- **POST** `/answer` → Add an answer to a question
- **GET** `/answers?question_id=123` → Retrieve answers for a specific question







