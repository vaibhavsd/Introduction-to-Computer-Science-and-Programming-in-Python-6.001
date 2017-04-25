import math
import random
import string
import copy
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3))-1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n-1):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    x= '*'
    hand[x] = hand.get(x, 0) + 1

    return hand

def update_hand(hand, word):
    word_lower= word.lower()
    new_hand= copy.deepcopy(hand)
    for i in word_lower:
        if i in new_hand.keys():
            new_hand[i] -= 1
            if new_hand[i]<0:
                new_hand[i]= 0
    return new_hand

def is_valid_word(word, hand, word_list):
    word_lower= word.lower()
    new_hand= copy.deepcopy(hand)
    for char in word_lower:
        if char not in new_hand:
            return False
        elif char in new_hand and new_hand[char]>0:
            new_hand[char] -= 1
        else:
            return False

    word_combinations= ""
    for chari in VOWELS:
        word_combinations += word_lower.replace("*", chari)
        word_combinations += " "

    list= word_combinations.split()
    for i in list:
        if i in word_list:
            return True
    return False

def substitute_hand(hand, letter):
    n_hand= copy.deepcopy(hand)
    string = ''.join(n_hand.keys())
    if letter not in string:
        return hand
    else:
        alphabets = VOWELS + CONSONANTS
        for chari in string:
            alphabets= alphabets.replace(chari, "")

        val= n_hand[letter]
        del(n_hand[letter])
        x = random.choice(alphabets)
        n_hand[x]= val
        return n_hand




subs= input("Would you like to substitute a letter? ")
print(subs)
if subs == 'yes':
    print('hi')