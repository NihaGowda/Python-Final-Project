import json
import random
import os
from pathlib import Path


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class QuizEngine:
    def __init__(self, questions_path: str | Path = None):
        # Safe default path: project_root/data/questions.json
        if questions_path is None:
            project_root = Path(__file__).resolve().parents[1]
            questions_path = project_root / "data" / "questions.json"

        questions_path = Path(questions_path)

        try:
            with open(questions_path, "r", encoding="utf-8") as f:
                self.questions = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"questions.json not found at: {questions_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in questions file: {questions_path}") from e

    def run(self, difficulty: str) -> int:
        difficulty = difficulty.strip().lower()

        if difficulty not in self.questions:
            print("Invalid difficulty selected.")
            return 0

        pool = self.questions[difficulty]
        if len(pool) < 5:
            print(f"Not enough questions in '{difficulty}' pool. Need at least 5.")
            return 0

        questions = random.sample(pool, 5)

        score = 0
        hints_used = 0
        max_hints = 2
        correct_count = 0

        for i, q in enumerate(questions, 1):
            # Copy options, shuffle, and keep the answer correct
            options = list(q["options"])
            correct_text = options[q["answer"]]
            random.shuffle(options)
            correct_index = options.index(correct_text)

            while True:
                clear()
                print(f"Question {i}/5  |  Difficulty: {difficulty.capitalize()}")
                print(f"Hints used: {hints_used}/{max_hints}\n")
                print(q["question"], "\n")

                for idx, opt in enumerate(options, 1):
                    print(f"{idx}. {opt}")

                print("\nH = Hint (-3 points) | Q = Quit round")
                choice = input("Your choice (1-4/H/Q): ").strip().lower()

                if choice == "q":
                    clear()
                    print("Exiting round early...")
                    input("Press Enter...")
                    return score

                if choice == "h":
                    if hints_used >= max_hints:
                        print("\nHint limit reached for this round.")
                        input("Press Enter...")
                        continue

                    print("\nHint:", q.get("hint", "No hint available."))
                    hints_used += 1
                    score -= 3
                    input("\nPress Enter to continue...")
                    continue

                if choice.isdigit() and 1 <= int(choice) <= 4:
                    picked = int(choice) - 1
                    if picked == correct_index:
                        print("\nCorrect!")
                        score += 10
                        correct_count += 1
                    else:
                        print("\nWrong.")
                        print("Answer:", options[correct_index])
                    input("\nPress Enter...")
                    break

                print("\nInvalid input. Please enter 1-4, H, or Q.")
                input("Press Enter...")

        clear()
        print("=== Round Summary ===")
        print(f"Correct: {correct_count}/5")
        print(f"Hints used: {hints_used}/{max_hints}")
        print(f"Round Score: {score}")
        input("\nPress Enter...")
        return score
