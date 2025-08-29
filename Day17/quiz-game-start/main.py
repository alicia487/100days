from question_model import Question
from data import question_data


question = Question()

def question_bank(self):
    questions = []
    for q_data in self.question:
        question_text = q_data["text"]
        question_answer = q_data["answer"]
    return questions


