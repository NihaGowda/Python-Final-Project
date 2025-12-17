import json
import random
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

class QuizEngine:
    def __init__(self):
        with open("data/questions.json") as f:
            self.questions = json.load(f)

    def run(self, difficulty):
        pool = self.questions[difficulty]
        questions = random.sample(pool, 5)

        score = 0

        for i, q in enumerate(questions, 1):
            clear()
            print(f"Question {i}/5\n")
            print(q["question"], "\n")

            for idx, opt in enumerate(q["options"]):
                print(f"{idx+1}. {opt}")

            print("\nH = Hint (-3 points)")
            choice = input("Your choice: ").strip()

            if choice.lower() == "h":
                print("\nHint:", q["hint"])
                score -= 3
                input("Press Enter...")
                choice = input("Your answer: ")

            if choice.isdigit() and int(choice)-1 == q["answer"]:
                print("\nCorrect!")
                score += 10
            else:
                print("\nWrong.")
                print("Answer:", q["options"][q["answer"]])

            input("\nPress Enter...")

        return score
