
wordlist= "hello my boy you go out of the window"

list= wordlist.split()

# print(list[1])
# print(len(list))


def match_with_gaps(guess, actual):

    # Check the lengths
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


def show_possible_matches(guess):
    my_wordlist= wordlist.split()
    list= ""
    for i in range(len(my_wordlist)):
        if match_with_gaps(guess, my_wordlist[i]):
            list += my_wordlist[i]
            list += " "
    if not list:
        return "No matches found"
    else:
        return list


sentlist= show_possible_matches("_ i_ _ _ _ ")

print(sentlist)


# print(match_with_gaps("a_ ple","apple"))