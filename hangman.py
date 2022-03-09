#hangman.py
# Stanalone file to play hangman

# Import module
from words import words
import random
import string

# Hangman picture
hangman_pic = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
      ===''']

# Function: Hangman
def Hangman():
    # Set up game
    word = random.choice(words).upper() # get a word from words.py
    letters = set(word) # get letter from word
    alphabet = set(string.ascii_uppercase) # get all alphabet
    used_letters = set() # letters user has guessed
    lp = 0 # set up the life point

    # Game start
    while len(letters) > 0 and lp < 6:
        print("==============================================")
        print(hangman_pic[lp]) # show hangman picture
        used_letters_list = " ".join(sorted(used_letters))
        print("Letters you have guess: ", used_letters_list) # show letters already used
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("The answer: ", " ".join(word_list)) # show letters of answer

        letters_guess = input("Let's guess a letter!: ").upper() # get input letters
        # User has guess letters
        if letters_guess in used_letters:
            print(f'This "{letters_guess}" character has been used.')
        # New letters
        elif letters_guess in alphabet - used_letters:
            used_letters.add(letters_guess) # add new letters
            # Check the answer
            if letters_guess in letters:
                letters.remove(letters_guess)
                print('Correct.')
            else:
                print('Miss.')
                lp+=1
        # Not alphabet
        else:
            print("Invalid character.")

    # You die
    if lp == 6:
        print("==============================================")
        print(hangman_pic[lp])
        print(f"You lose. The answer is '{word}'")
    # You win
    else:
        print(f"Congrats! The answer is '{word}'")

# Run function
Hangman()