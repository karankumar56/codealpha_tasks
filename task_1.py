#Hangman Game

import random

def hangman_game():
    
    word_list = ['apple', 'banana', 'grape', 'orange', 'peach']
    chosen_word = random.choice(word_list)
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print("_ " * len(chosen_word))

    while attempts_left > 0:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("Good guess!")
        else:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")

        
        display_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word.strip())

        
        if all(letter in guessed_letters for letter in chosen_word):
            print("Congratulations! You guessed the word!")
            break
    else:
        print(f"Game over! The word was '{chosen_word}'.")


hangman_game()