
# Playing with the strings
# s= 'abcdef'
#
# print(s[-3])
# print(s[-1])
# print(s[0])
#
# # s[start:stop:step]
# print(s[1:6:1])
# print(s[::-1])
#
# #####################################################################
# for var in range(4):
#     print(1)
#
# for var in range(4,5):
#     print(2)
#
# #####################################################################
# s= "abcdefghiu"
# for n in range(len(s)):
#     if s[n]=="i" or s[n]=="u":
#         print("There is an i or u!")
#
#
# for n in s:
#     if n=='i' or n=='u':
#         print("There is an i or u!")
#####################################################################

# The Cheer Leader girls code
#
# an_letters= "aefhilmnorsxAEFHILMNORSX"
# word= input("I'll cheer you up!\nGive me a word: ")
# times= int(input("Inspiration level (0-10): "))
#
# for i in word:
#     if i in an_letters:
#         print(i)
#         print("Give me an " + i + " ------" + i + "!!" + "\n")
#     else:
#         print(i)
#         print("Give me a " + i + " ------" + i + "!!" + "\n")
#
# for i in range(times):
#     print(word + "!!!" + "\n")

#####################################################################

# The number guessing code
# Six tries it is! No more than that!

epsilon = 0.1
print("This is a cube root solver!")
number = int(input("Enter a number for which you wish to find a cube root: "))
guess = 1

cr = guess
j = 1

while cr**3< number:
    if number - cr**3 <= 10:
        print("The cube root of the number is:", int(cr))
        j = 0
        break
    else:
        cr += epsilon

if j != 0:
    print("The cube root of the number is:", int(cr))