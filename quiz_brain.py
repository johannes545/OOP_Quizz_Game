class QuizBrain:

    def __init__(self, question_list):
        self.number = 0
        self.question = question_list
        self.score = 0

    def still_has_questions(self):
        return self.number < len(self.question)

    def new_question(self):
        current_question = self.question[self.number]
        self.number += 1
        user_answer = input(f"Q.{self.number}: {current_question.question} (True/False)?")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer,  correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("correct")
            self.score += 1
        else:
            print("wrong")
        print(f"the correct answer to the question {correct_answer}")
        print(f"Your current score is: {self.score}/{self.number}")
        print("\n")

