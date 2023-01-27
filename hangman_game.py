import random

all_words = ["apple", "computer", "tv", "bike", "game", "greating", "magic", "roof", "fish", "orange", "laptop", "love", "lamp"]
current_word = f"{all_words[random.randint(0, len(all_words) - 1)]}"
len_current_word = len(current_word)
sum_of_latter = ""

# -------------------------------------------------------------------------------------------------------------------------------

print("Hangman - GAME")

print(current_word)
print(len_current_word)

while True:

    answer_latter = input("Enter your latter: ").lower()[0]

    if answer_latter in current_word:
        sum_of_latter += answer_latter
        len_current_word -= 1
        print(current_word)
        print(f"Lucky! Gussed right - {answer_latter.upper()}! Left {len_current_word}!")
    else:
        print("Try again!")

    if set(sum_of_latter) == set(current_word):
        print("YOU GUSSED ALL THE RIGHT LATTER! REPLACE!")
