import random

human_score = 0
computer_score = 0
for i in range(5):
    hand = input("Rock Paper Scissors? ")
    computer = random.choice(["Rock", "Paper", "Scissors"])
    print(f"Computer's hand {computer}")
    if hand == computer:
        print("Epic Draw")
    elif hand == "Rock" and computer == "Paper":
        print("Epic Loss")
        computer_score += 1
    elif hand == "Rock" and computer == "Scissors":
        print("Epic Win")
        human_score += 1
    elif hand == "Paper" and computer == "Scissors":
        print("Epic Loss")
        computer_score += 1
    elif hand == "Paper" and computer == "Rock":
        print("Epic Win")
        human_score += 1
    elif hand == "Scissors" and computer == "Paper":
        print("Epic Win")
        human_score += 1
    elif hand == "Scissors" and computer == "Rock":
        print("Epic Loss")
        computer_score += 1
    print(f"Human score={human_score}")
    print(f"Computer score ={computer_score}")
if human_score > computer_score:
    print("Human Won")
elif computer_score > human_score:
    print("Computer Rules")
else:
    print("Draw")