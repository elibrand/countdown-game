# word_bank is a list of words that are nine or more letters in length
import random

with open("game/wordlist.txt", "r") as f:
    word_bank = []

    for x in f:
        word_bank.append(x.strip())

guess_list = []

for word in word_bank:
    if len(word) > 9:
        guess_list.append(word)


def get_scram():
    """
    scrambles a random word nine letters or more
    :return: an uppercase word as described
    """
    guess_word = random.choice(guess_list)

    char_list = list(guess_word)

    random.shuffle(char_list)

    scram_word = ''.join(char_list)

    scram_word = scram_word.upper()

    return scram_word


def check_word(guess):
    """
    checks to see if is real and if it's in the guess word
    :param guess: the word that might not be a real word
    :return: True if it's in the word_bank
    """
    if guess.lower() in word_bank:
        return True


def check_if_in(guess, scram_word):
    """
    checks if the word guessed is in the jumbled word
    :param guess: small word
    :param scram_word: big word
    :return: whether all the letters in the first word show up only once in the second
    """
    g_list = list(guess.upper())

    gw_list = list(scram_word)

    for letter in g_list:
        if letter in gw_list:
            gw_list.remove(letter)
        else:
            return False
    return True



