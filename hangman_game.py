import random

all_words = ["apple", "computer", "tv", "bike", "game", "greating", "magic", "roof", "fish", "orange", "laptop", "love", "lamp"]
current_word = f"{all_words[random.randint(0, len(all_words) - 1)]}"
len_current_word = len(current_word)
sum_of_latter = ""

print("Hangman - GAME")

print(f"First latter of the word: {current_word[0]}, the last latter {current_word[-1]}")

while True:

    answer_latter = input("Enter your latter: ").lower()[0]

    if answer_latter in current_word:
        sum_of_latter += answer_latter
        len_current_word -= 1
        print(f"Lucky! Gussed right latter - {answer_latter.upper()}! Left latters {len_current_word}!")
    else:
        print("Try again!")

    if sum_of_latter == current_word:
        print("YOU ARE WIN!")
    elif set(sum_of_latter) == set(current_word):
        print("YOU GUSSED ALl! REPLACE THE LATTERS!")
        answer_word = input("Enter the word: ").lower()

        if answer_word == current_word:
            print("YOU ARE WIN!")
        else:
            print("You are lose!")
