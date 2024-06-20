# Problem Set 2, hangman.py
# Name: John Harlow
# Collaborators:
# Time spent: 15:57 -> 18:16 :: 2 hours and 19 mins

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
from typing import List

WORDLIST_FILENAME = "psets/02/words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist: List[str]):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word: str, letters_guessed: List[str]) -> bool:
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """

    return True if all(char in letters_guessed for char in list(secret_word)) else False


def get_guessed_word(secret_word: str, letters_guessed: List[str]) -> str:
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    char_redacted_if_not_guessed = lambda char: char if char in letters_guessed else "_"
    return "".join(map(char_redacted_if_not_guessed, list(secret_word)))


def get_available_letters(letters_guessed: List[str]) -> str:
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """

    char_not_guessed = lambda char: char not in letters_guessed
    return "".join(filter(char_not_guessed, string.ascii_lowercase))


def get_total_score(guesses_remaining: int, secret_word: str) -> int:
    return guesses_remaining * len(set(secret_word))


def display_starting_message(secret_word: str, warnings_remining: int) -> None:
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    print(f"You have {warnings_remining} warnings left")


secret_word = "else"


def hangman(secret_word: str):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """

    VOWELS: List[str] = ["a", "e", "i", "o", "u"]
    GUESSES_ALLOWED: int = 6
    guesses_remaining: int = GUESSES_ALLOWED
    WARNINGS_ALLOWED: int = 3
    warnings_remining: int = WARNINGS_ALLOWED
    letters_guessed: List[str] = []

    display_starting_message(secret_word, warnings_remining)
    while not is_word_guessed(secret_word, letters_guessed):
        print("-------------")
        if guesses_remaining == 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
            break

        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")

        char = input("Please guess a letter: ")[0].lower()

        if not char.isalpha() or char in letters_guessed:
            valid_char_m = "That is not a valid letter"
            prev_guess_m = "You've already guessed that letter."
            issue_message: str = valid_char_m if not char.isalpha() else prev_guess_m
            if warnings_remining > 0:
                warnings_remining -= 1
                print(
                    f"Oops! {issue_message} You have {warnings_remining} warnings left: {get_guessed_word(secret_word, letters_guessed)}"
                )
            else:
                guesses_remaining -= 1
                print(
                    f"Oops! {issue_message} You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}"
                )
            continue

        letters_guessed.append(char)
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if char in secret_word:
            print("Good guess:", guessed_word)
        else:
            print("Oops! That letter is not in my word:", guessed_word)
            guesses_remaining -= 2 if char in VOWELS else 1

    if is_word_guessed(secret_word, letters_guessed):
        print("-------------")
        print("Congratulations, you won!")
        total_score = get_total_score(guesses_remaining, secret_word)
        print(f"Your total score for this game is: {total_score}")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word: str, other_word: str) -> bool:
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    return all(char == "_" or char == other_word[i] for i, char in enumerate(my_word))


def show_possible_matches(my_word: str) -> None:
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """

    matches = ", ".join(
        filter(
            lambda word: len(my_word) == len(word) and match_with_gaps(my_word, word),
            wordlist,
        )
    )
    print(matches) if len(matches) > 0 else print("No matches found")


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    VOWELS: List[str] = ["a", "e", "i", "o", "u"]
    GUESSES_ALLOWED: int = 6
    guesses_remaining: int = GUESSES_ALLOWED
    WARNINGS_ALLOWED: int = 3
    warnings_remining: int = WARNINGS_ALLOWED
    letters_guessed: List[str] = []

    display_starting_message(secret_word, warnings_remining)
    while not is_word_guessed(secret_word, letters_guessed):
        print("-------------")
        if guesses_remaining == 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
            break

        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")

        current_guessed_word = get_guessed_word(secret_word, letters_guessed)
        char = input("Please guess a letter: ")[0].lower()

        if char == "*":
            show_possible_matches(current_guessed_word)
            continue
        elif not char.isalpha() or char in letters_guessed:
            valid_char_m = "That is not a valid letter"
            prev_guess_m = "You've already guessed that letter."
            issue_message: str = valid_char_m if not char.isalpha() else prev_guess_m
            if warnings_remining > 0:
                warnings_remining -= 1
                print(
                    f"Oops! {issue_message} You have {warnings_remining} warnings left: {current_guessed_word}"
                )
            else:
                guesses_remaining -= 1
                print(
                    f"Oops! {issue_message} You have no warnings left so you lose one guess: {current_guessed_word}"
                )
            continue

        letters_guessed.append(char)
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if char in secret_word:
            print("Good guess:", guessed_word)
        else:
            print("Oops! That letter is not in my word:", guessed_word)
            guesses_remaining -= 2 if char in VOWELS else 1

    if is_word_guessed(secret_word, letters_guessed):
        print("-------------")
        print("Congratulations, you won!")
        total_score = get_total_score(guesses_remaining, secret_word)
        print(f"Your total score for this game is: {total_score}")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # To test part 2 uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    # To test part 3 uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
