#create a hangmang project in which a computer chooses a random word, replaces it with blanks
# and the user has to guess the word by guessing the letters in the word
# the user has 6 chances to guess the word
# if the user guesses the word, the user wins
# if the user does not guess the word, the user loses

import random

words = ['mouse', 'tree', 'apple', 'elephant', 'camel']

word = random.choice(words)
word = word.lower()

place_holder = "_" * len(word)
correct_l = []

chances = 6
incorrect_guesses = []

hangman_pics = [
    '''
     -----
     |   |
         |
         |
         |
         |
    ''', '''
     -----
     |   |
     O   |
         |
         |
         |
    ''', '''
     -----
     |   |
     O   |
     |   |
         |
         |
    ''', '''
     -----
     |   |
     O   |
    /|   |
         |
         |
    ''', '''
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    ''', '''
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    ''', '''
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    '''
]

# Game loop
while chances > 0:
    print(hangman_pics[6 - chances])
    print(f"Word to guess: {place_holder}")
    print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
    guess = input("Enter a letter: ").lower()

    if guess in correct_l or guess in incorrect_guesses:
        print("You already guessed that letter.")
        continue
    
    if guess in word:
        correct_l.append(guess)
        place_holder = "".join([char if char in correct_l else "_" for char in word])
        if "_" not in place_holder:
            print(f"Congratulations! You won. The word was: {word}")
            break
    else:
        incorrect_guesses.append(guess)
        chances -= 1
        if chances == 0:
            print(hangman_pics[6])
            print(f"You lost! The word was: {word}")
            break


