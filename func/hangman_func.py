#hangman_func.py
# function to integrate with GUI for Hangman

# module
from words import words
import random
import string

# hangman picture
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

# return value with initial state
def StartGame():
    # create letter, used_letter and last_chr dict
    letters = {}
    used_letters = {}
    last_chr = {}

    # get word and its length
    word = random.choice(words).upper()
    word_len = len(word)

    # initiate letters
    letters["gui"] = " ".join(["-" for i in range(word_len)])
    letters["playgame_str"] = word
    letters["playgame_set"] = set(word)

    # initiate used_letters
    used_letters["gui"] = "" # letters user has guessed
    used_letters["playgame_str"] = ""
    used_letters["playgame_set"] = set()

    lp = 6 # set up the life point
    last_chr["character"] = ""
    last_chr["check"] = ""

    return letters, used_letters, lp, last_chr

# return value after guessing
def PlayGame(letters_guess_param, letters_param, used_letters_param, lp_param):
    # get date for checking later
    letters_guess = letters_guess_param.upper()
    letters = letters_param
    letters_set = letters["playgame_set"]
    used_letters = used_letters_param
    used_letters_set = used_letters["playgame_set"]
    lp = lp_param
    last_chr = {}
    alphabet = set(string.ascii_uppercase)

    # user has guess letters
    if letters_guess in used_letters_set:
        last_chr["character"] = letters_guess
        last_chr["check"] = "Repeat"
    # new letters
    elif letters_guess in alphabet - used_letters_set:
        used_letters_set.add(letters_guess) # add new letters
        # right awnser
        if letters_guess in letters_set:
            letters_set.remove(letters_guess)
            last_chr["character"] = letters_guess
            last_chr["check"] = "Correct"
        # wrong awnser
        else:
            last_chr["character"] = letters_guess
            last_chr["check"] = "Miss"
            lp = lp - 1
    # not alphabet
    else:
        last_chr["character"] = letters_guess
        last_chr["check"] = "Invalid character"

    # update letters and used_letters for displaying
    letters["gui"] = [letter if letter in used_letters_set else "-" for letter in letters["playgame_str"]]
    used_letters["gui"] = " ".join(sorted(used_letters_set))

    # you die
    if lp == 0:
        last_chr["check"] = "LOSE"
        return letters, used_letters, lp, last_chr
    # you win
    if len(letters_set) == 0:
        last_chr["check"] = "WIN"
        return letters, used_letters, lp, last_chr

    return letters, used_letters, lp, last_chr