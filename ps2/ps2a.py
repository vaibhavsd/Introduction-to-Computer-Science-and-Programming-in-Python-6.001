def is_word_guessed (secret_word, letters_guessed):
    count = 0
    for chari in secret_word:
        for charj in letters_guessed:
            if chari== charj:
                print("match found")
                count += 1

    if count == len(secret_word):
        return True
    else: return False


def get_guessed_word (secret_word, letters_guessed):
    string= ""
    for chari in secret_word:
        count = 0
        for charj in letters_guessed:
            if chari== charj:
                count = 1
                string += chari
                break
        if count is not 1:
            string += ("_ ")
    return string

def get_available_letters(letters_guessed):
    clist= "abcdefghijklmnopqrstuvwxyz"
    string= ""
    for chari in clist:
        count= 0
        for charj in letters_guessed:
            if chari== charj:
                count = 1
                break
        if count== 0:
            string += chari
    return string



# secret_word = 'apple'
letters_guessed = ['e','i','k','p','r','s']
# print(get_guessed_word(secret_word, letters_guessed))
print(get_available_letters(letters_guessed))