from src.quiz import QuizEngine
from src.learn import run_learn_mode

class GameEngine:
    def run_main_menu(self, player, levels=None):
        while True:
            print("\n==== MAIN MENU ====")
            print("1. Learn Mode")
            print("2. Challenge Mode")
            print("3. Exit")

            choice = input("Choose: ")

            if choice == "1":
                run_learn_mode()
            elif choice == "2":
                self.challenge(player)
            elif choice == "3":
                break

    def challenge(self, player):
        quiz = QuizEngine()

        print("\n--- Challenge Mode ---")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("0. Back")

        diff = {"1":"easy","2":"medium","3":"hard"}
        choice = input("Difficulty: ")

        if choice == "0":
            return
        if choice not in diff:
            return

        score = quiz.run(diff[choice])
        player.score += score

        print("\nRound Score:", score)
        print("Total Score:", player.score)
        input("Press Enter...")
