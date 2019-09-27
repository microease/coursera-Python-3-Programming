# coding:utf-8
# Author :     microease
# Date :       2019/4/16

# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.

# f = open('travel_plans.txt')
# num = 0
# nums = []
# for line in f:
#     for word in line:
#         nums.append(word)
# num = len(nums)
# f.close()

# We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.

# f = open('emotion_words.txt')
# num_word = [word for line in f for word in line.split()]
# num_words = len(num_word)
# f.close()

# Assign to the variable num_lines the number of lines in the file school_prompt.txt.
# f = open("school_prompt.txt")
# num_lines = 0
# for line in f:
#     num_lines += 1

# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
# fname = "school_prompt.txt"
# with open(fname, 'r') as f:
#     beginning_chars = f.read(30)

# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
# f = open('school_prompt.txt')
# lines = []
# lines_2 = []
# three = []
# #读取文件，分行
# for line in f:
#     lines.append(line)
# #将每一行用空格分开
# for line in lines:
#     lines_2.append(line.split())
# # 将第三个单词加入到three
# for line in lines_2:
#     three.append(line[2])
# print(three)

# Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
# f = open('emotion_words.txt')
# lines = []
# lines_2 = []
# emotions = []
# #读取文件，分行
# for line in f:
#     lines.append(line)
# #将每一行用空格分开
# for line in lines:
#     lines_2.append(line.split())
# # 将第三个单词加入到three
# for line in lines_2:
#     emotions.append(line[0])
# print(emotions)

# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
# f = open('travel_plans.txt')
# first_chars = []
# for line in f:
#     for char in line:
#         first_chars.append(char)
# first_chars = ''.join(first_chars[0:33])
# print(first_chars)

# Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
f = open('school_prompt.txt')
p_words = []
lines = []
for line in f:
    lines.append(line.split())
for line in lines:
    for word in line:
        if 'p' in word:
            p_words.append(word)
print(p_words)