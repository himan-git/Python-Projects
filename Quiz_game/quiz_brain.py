class QuizBrain:
    score = 0
    want_to_continue = True

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)? "
        )
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Your answer is correct!")
            self.score += 1
        else:
            print("Your ans is wrong!")
        print(f"Correct answer was: {correct_answer}")
        print(f"your current score is: {self.score} / {self.question_number}")
        wtc = input("Do you want too continue the GAME ?  (Y / N)").lower()
        if wtc == "n":
            self.want_to_continue = False
        print("\n")
