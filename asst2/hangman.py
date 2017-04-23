# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
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


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    ###################################################
    count = 0
    for chari in secret_word:
        for charj in letters_guessed:
            if chari == charj:
                # print("match found")
                count += 1

    if count == len(secret_word):
        return True
    else:
        return False
    ####################################################


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #####################################################
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
    ######################################################


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    ######################################################
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
    #######################################################
    
    

def hangman(secret_word):
    '''
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
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #########################################################################
    print("\n \n")
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word),"letters long.")
    print("............")

    guess_count = 6
    guess_list =""
    warnings= 4
    game_status = 0
    letters_guessed = ""
    go_forward = 1
    vowels= "aeiou"

    while guess_count>0 and game_status is 0:
    # for i in range(10):

        print("\n \n")
        print("Word:", get_guessed_word(secret_word, letters_guessed))
        if guess_count>1:
            print("You have", guess_count,"guesses left.")
        else:
            print("You are left with one last guess.")

        print("Available letters: ", get_available_letters(letters_guessed))

        guess= input("Please guess a letter: ")
        if str.isalpha(guess):
            guess= str.lower(guess)
        else:
            print("That is not a valid letter.")
            if warnings>0:
                warnings -= 1
                print("You have", warnings, "warnings left")
                go_forward= 0
            else:
                guess_count -=1
                print("You lose a guess! ")
                print("You have", warnings, "warnings left")
                go_forward = 0

        if guess in guess_list:
            print("You have already guessed that letter.")
            if warnings>0:
                warnings -= 1
                print("You have", warnings, "warnings left")
                go_forward= 0
            else:
                guess_count -=1
                print("You lose a guess! ")
                print("You have", warnings, "warnings left")
                go_forward = 0


        if go_forward is 1:
            guess_list += guess
            if guess in secret_word:
                letters_guessed += guess
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                print("............")
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                if guess in vowels:
                    guess_count -= 2
                else:
                    guess_count -= 1


        if is_word_guessed(secret_word, letters_guessed):
            game_status =1
            print("\n \nWohoo! You have won the game!")
            print("Your total score for this game is:", guess_count*len(''.join(set(secret_word))))

    if game_status is 0:
        print("\n \nSorry, you ran out of guesses.")
        print("The word was:", secret_word)

    ##############################################################################





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #######################################################
    # Check the lengths
    guess= my_word
    actual= other_word
    guess_len= len(guess.replace(" ", ""))
    actual_len= len(actual.replace(" ", ""))
    if guess_len != actual_len:
        return False

    guessword= guess.replace(" ", "")
    space= "_"
    n= len(guessword)
    for i in range(n):
        if guessword[i] is space:
            pass
        elif guessword[i] is not actual[i]:
            return False
    return True
    #########################################################





def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    ##############################################################
    guess= my_word
    my_wordlist= wordlist
    list= ""
    for i in range(len(my_wordlist)):
        if match_with_gaps(guess, my_wordlist[i]):
            list += my_wordlist[i]
            list += " "
    if not list:
        return "No matches found"
    else:
        return list
    ##############################################################




def hangman_with_hints(secret_word):
    '''
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
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #########################################################################
    print("\n \n")
    print("Welcome to the game Hangman (with hints *)!")
    print("I am thinking of a word that is", len(secret_word),"letters long.")
    print("............")

    guess_count = 6
    guess_list =""
    warnings= 4
    game_status = 0
    letters_guessed = ""
    go_forward = 1
    vowels= "aeiou"

    while guess_count>0 and game_status is 0:
    # for i in range(10):
        go_forward =1
        print("\n \n")
        print("Word:", get_guessed_word(secret_word, letters_guessed))
        if guess_count>1:
            print("You have", guess_count,"guesses left.")
        else:
            print("You are left with one last guess.")

        print("Available letters: ", get_available_letters(letters_guessed))

        guess= input("Please guess a letter: ")
        if guess is "*":
            lettr_guessed= letters_guessed.replace("_ ", "")
            if not lettr_guessed:
                print("You need to guess at least one letter before using hints")
                go_forward =0
            else:
                print("Possible word matches are: ")
                print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
                go_forward = 0

        elif str.isalpha(guess):
            guess= str.lower(guess)
        else:
            print("That is not a valid letter.")
            if warnings>0:
                warnings -= 1
                print("You have", warnings, "warnings left")
                go_forward= 0
            else:
                guess_count -=1
                print("You lose a guess! ")
                print("You have", warnings, "warnings left")
                go_forward = 0

        if guess in guess_list:
            print("You have already guessed that letter.")
            if warnings>0:
                warnings -= 1
                print("You have", warnings, "warnings left")
                go_forward= 0
            else:
                guess_count -=1
                print("You lose a guess! ")
                print("You have", warnings, "warnings left")
                go_forward = 0


        if go_forward is 1:
            guess_list += guess
            if guess in secret_word:
                letters_guessed += guess
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                print("............")
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                if guess in vowels:
                    guess_count -= 2
                else:
                    guess_count -= 1


        if is_word_guessed(secret_word, letters_guessed):
            game_status =1
            print("\n \nWohoo! You have won the game!")
            print("Your total score for this game is:", guess_count*len(''.join(set(secret_word))))

    if game_status is 0:
        print("\n \nSorry, you ran out of guesses.")
        print("The word was:", secret_word)




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # secret_word = "tact"
    # print(secret_word)
    # hangman(secret_word)


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

    # print(match_with_gaps("te_ t", "tact"))
    # print(match_with_gaps("a_ _ le", "banana"))
    # print(match_with_gaps("a_ _ le", "apple"))
    # print(match_with_gaps("a_ ple", "apple"))
    #
    # print(show_possible_matches("t_ _ t"))
    # print(show_possible_matches("abbbb_ "))
    # print(show_possible_matches("a_ pl_ "))
