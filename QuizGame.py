
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question["text"])
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")

    def get_user_answer(self):
        while True:
            try:
                user_answer = int(input("Your answer: "))
                if 1 <= user_answer <= len(self.current_question["options"]):
                    return user_answer
                else:
                    print("Please enter a valid option.")
            except ValueError:
                print("Please enter a valid number.")

    def check_answer(self, user_answer):
        correct_option = self.current_question["answer"]
        if user_answer == correct_option:
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_option}.")

    def run_quiz(self):
        for i, question in enumerate(self.questions, 1):
            self.current_question = question
            print(f"\nQuestion {i}/{len(self.questions)}:")
            self.display_question(question)
            user_answer = self.get_user_answer()
            self.check_answer(user_answer)

        print(f"\nFinal Score: {self.score}/{len(self.questions)}")


# Example usage
questions = [
    {"text": "What is the capital of Lakshadweep?", "options": ["Kavaratti", "Delhi", "Kerala"], "answer": 1},
    {"text": "In which college in Madhya Pradesh is the first drone school located?", "options": ["Sgsits Indore", "Mits Gwalior", "Sirt Bhopal"], "answer": 2},
    {"text": "How many times the hands of a clock coincide in a day?", "options": ["24", "22", "11"], "answer": 2},
]

quiz = Quiz(questions)
quiz.run_quiz()

