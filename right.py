import random
import time
from tabulate import tabulate

questions = [
    "[(6 + 4) * 2^2 - 8] ÷ 4",
    "(5 + 3 * 2)^2 ÷ (4 + 2)",
    "60 ÷ [(4 + 2) * (3 + 1)]",
    "[(2 + 3) * (4 + 1)^2 - 10] ÷ 5",
    "[(16 ÷ 4) + (3 * 2)]^2",
    "(8 + 2) * [6 - (3 + 1)]",
    "100 ÷ [(2 * 5) + (3^2)]",
    "[(5 * 3)^2 - (6 + 3) * 2] ÷ 3",
    "[(7 + 1) * 2 + (10 - 4)]^2",
    "[(12 ÷ 3) + (2^2 + 1)] * 2"
]

options = [
    ["A. 12", "B. 10", "C. 09", "D. 08"],
    ["A. 20.36", "B. 20.16", "C. 20.54", "D. 20.76"],
    ["A. 2.3", "B. 2.6", "C. 2.5", "D. 2.4"],
    ["A. 22", "B. 23", "C. 25", "D. 33"],
    ["A. 100", "B. 103", "C. 98", "D. 108"],
    ["A. 22", "B. 29", "C. 20", "D. 25"],
    ["A. 5.27", "B. 5.36", "C. 5.26", "D. 5.29"],
    ["A. 68", "B. 71", "C. 65", "D. 69"],
    ["A. 484", "B. 489", "C. 481", "D. 476"],
    ["A. 13", "B. 28", "C. 35", "D. 18"]
]

answers = ["D", "B", "C", "B", "A", "C", "C", "D", "A", "D"]

quiz_data = list(zip(questions, options, answers))
random.shuffle(quiz_data)

guesses = []
score = 0

print("\n📘 WELCOME TO THE MATH QUIZ GAME 📘")

for i, (question, opts, correct) in enumerate(quiz_data, start=1):
    print(f"\nQ{i}. {question}")
    print(tabulate([[opt] for opt in opts], tablefmt="fancy_grid"))

    while True:
        guess = input("👉 Enter your answer (A, B, C, D): ").upper()
        if guess in ["A", "B", "C", "D"]:
            break
        else:
            print("⚠️ Invalid input!")

    guesses.append(guess)

    if guess == correct:
        print("✅ CORRECT!")
        score += 1
    else:
        print(f"❌ INCORRECT! Correct Answer: {correct}")

    time.sleep(0.5)

print("\nRESULTS")
print(f"Score: {score}/{len(quiz_data)}")