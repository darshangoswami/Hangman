import random
import string

from words import words


def get_valid_word(wordlist):
    word = random.choice(wordlist)
    while '-' in wordlist or '' in wordlist:
        word = random.choice(wordlist)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # guessed letters

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left and you've used these letters: ", "".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", "".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in word")

        elif user_letter in used_letters:
            print("You've already used that letter.")

        else:
            print("Invalid character")

    if lives == 0:
        print(f"You died, the word was {word}.")
    else:
        print(f"You got all the letters correct of the word: {word}")

hangman()
