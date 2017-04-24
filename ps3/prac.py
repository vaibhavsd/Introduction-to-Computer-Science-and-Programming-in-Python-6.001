import copy


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
    for char in word_lower:
        if char not in hand.keys():
            return False
    if word_lower not in word_list:
        return False
    return True


# hand= {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
# word= 'quail'
# print(update_hand(hand, word))


hand= {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
word= 'Rapture'
word_list = ("rapture", "devil", "boy", "girl", "man")



print(is_valid_word(word, hand, word_list))




