import random

print("Guess the number - GAME")

random_num = random.randint(1, 10)

while True:
    answer = int(input("Enter the number: "))

    if answer == random_num:
        print("You are win!")
        break
    else:
        print("Try again!")
        continue
