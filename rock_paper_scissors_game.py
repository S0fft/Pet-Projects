import random

print("Rock Paper Scissors - Game")


def game():
    random_num_sign = random.randint(1, 3)

    if random_num_sign == 1:
        random_num_sign = "rock"
    elif random_num_sign == 2:
        random_num_sign = "paper"
    elif random_num_sign == 3:
        random_num_sign = "scissors"

    while True:
        answer = input("Choose your answer (ROCK | PAPER | SCISSORS): ").lower()

        if answer == random_num_sign:
            print(f"Draw! The computer answered: {random_num_sign.upper()}")
            break

        if answer == "rock" and random_num_sign == "paper":
            print(f"You are lose! The computer answered: {random_num_sign.upper()}")
            break
        elif answer == "rock" and random_num_sign == "scissors":
            print(f"You are win! The computer answered: {random_num_sign.upper()}")
            break

        if answer == "paper" and random_num_sign == "rock":
            print(f"You are win! The computer answered {random_num_sign.upper()}")
            break
        elif answer == "paper" and random_num_sign == "scissors":
            print(f"You are lose! The computer answered {random_num_sign.upper()}")
            break

        if answer == "scissors" and random_num_sign == "rock":
            print(f"You are lose! The computer answered {random_num_sign.upper()}")
            break
        elif answer == "scissors" and random_num_sign == "paper":
            print(f"You are win! The computer answered {random_num_sign.upper()}")
            break

        if answer != "rock" or answer != "paper" or answer != "scissors":
            print("Please enter the correct answer (GRAMMAR OR TYPE MISTAKE)!")
            break


game()

while True:
    revenge = input("Try again? (YES | NO): ")

    if revenge.lower() == "yes":
        game()
    elif revenge.lower() == "no":
        print("Game over, good luck!")
        break
    else:
        print("Please enter the correct answer (GRAMMAR OR TYPE MISTAKE)!")
