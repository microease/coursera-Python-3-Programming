# coding:utf8
# Author :       huxiaoyi
# Date：         2019-04-17
# Time：         00:56

# The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable credits. Do not hardcode this – use dictionary accumulation!

# Junior = {'SI 206': 4, 'SI 310': 4, 'BL 300': 3, 'TO 313': 3, 'BCOM 350': 1, 'MO 300': 3}
# credits = 0
# for i in list(Junior.values()):
#     credits+=i
# print(credits)

# Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.

# str1 = "peter piper picked a peck of pickled peppers"
# print(str1)
# freq = {}
# for i in str1:
#     freq[i] = str1.count(i)
# print(freq)

# Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.
#
# s1 = "hello"
# counts = dict()
# for i in s1:
#     counts[i] = s1.count(i)
# print(counts)

# Create a dictionary, freq_words, that displays each word in string str1 as the key and its frequency as the value.

# str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
# str1 = str1.split()
# print(str1)
# freq_words = {}
# for i in str1:
#     freq_words[i] = str1.count(i)
# print(freq_words)

# Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.
# sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
# sent = sent.split()
# print(sent)
# wrd_d  = {}
# for i in sent:
#     wrd_d [i] = sent.count(i)
# print(wrd_d )

# Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.
# sally = "sally sells sea shells by the sea shore"
# temp = []
# for i in sally:
#     temp.append(i)
# print(temp)
# characters = {}
# for i in temp:
#     characters[i] = temp.count(i)
# print(characters)
# best_char = 's'

# Do the same as above but now find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.
# sally = "sally sells sea shells by the sea shore and by the road"
# temp = []
# for i in sally:
#     temp.append(i)
# print(temp)
# characters = {}
# for i in temp:
#     characters[i] = temp.count(i)
# print(characters)
# worst_char = 'n'

# Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.
# string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
# string1 = string1.lower()
# letter_counts = {}
# for i in string1:
#     letter_counts[i] = string1.count(i)
# print(letter_counts)

# Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
p = p.lower()
low_d = {}
for i in p:
    low_d[i] = p.count(i)
print(low_d)