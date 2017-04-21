
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

an_letters= "aefhilmnorsxAEFHILMNORSX"
word= input("I'll cheer you up!\nGive me a word: ")
times= int(input("Inspiration level (0-10): "))

for i in word:
    print("Give me a " + i + " ------" + i + "!!" + "\n")

for i in range(times):
    print(word + "!!!" + "\n")


#####################################################################

# The number guessing code
# Six tries it is! No more than that!



