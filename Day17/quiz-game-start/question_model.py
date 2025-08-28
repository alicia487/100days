# Create a question class with an __init()__ method with two attributes: text and answer attribute
# 두 가지 속성(text 및 answer 속성)을 갖는 __init()__ 메서드로 질문 클래스를 만듭니다.

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

