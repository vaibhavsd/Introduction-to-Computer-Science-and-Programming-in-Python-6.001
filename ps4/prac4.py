# def get_permutations(sequence):
#     if len(sequence)==1:
#         return sequence
#     else:
#         letter= sequence[0]
#         list= get_permutations(sequence[1:len(sequence)])
#         new_list = []
#         for word in list:
#             for i in range(len(word)+1):
#                 new_list.append(word[:i] + letter + word[i:])
#         return new_list
#
#
# print(get_permutations('abn'))
# print(get_permutations('abns'))

str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list = [str1, str2]

shift= 4
dict= {}

for str in list:
    cnt=0
    for i in str:
        j= cnt + shift - 1
        if j<26:
            dict[i]= str[j]
        else:
            dict[i]= str[j-26]
        cnt +=1
