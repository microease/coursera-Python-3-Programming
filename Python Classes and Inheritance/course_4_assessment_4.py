# coding:utf-8
# File Name：     course_4_assessment_4
# Description :
# Author :       micro
# Date：          2019/10/30
# The code below takes the list of country, country, and searches to see if it is in the dictionary gold which shows some countries who won gold during the Olympics. However, this code currently does not work. Correctly add try/except clause in the code so that it will correctly populate the list, country_gold, with either the number of golds won or the string “Did not get gold”.
# 下面的代码获取国家/地区列表，并进行搜索以查看其是否在字典黄金中，该字典显示了在奥运会期间赢得金牌的一些国家。 但是，此代码当前不起作用。 在代码中正确添加try / except子句，以便它将使用赢得的金数或字符串“未获得金”正确填充country_gold列表。
gold = {"US": 46, "Fiji": 1, "Great Britain": 27, "Cuba": 5, "Thailand": 2, "China": 26, "France": 10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []
print(gold.keys())
for x in country:
    try:
        x in gold.keys()
        country_gold.append(gold[x])
    except KeyError:
        country_gold.append("Did not get gold")

print(country_gold)
# country_gold.append(gold[x])
# country_gold.append("Did not get gold")


# Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so that the code passes.
# 提供了一个越野车for循环，该循环试图从某些词典中累积一些值。 插入一个try / except，以便代码通过。

di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49},
      {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7},
      {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89},
      {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        diction.keys() == "Puppies"
        total = total + diction['Puppies']
    except:
        pass

print("Total number of puppies:", total)

# The list, numb, contains integers. Write code that populates the list remainder with the remainder of 36 divided by each number in numb. For example, the first element should be 0, because 36/6 has no remainder. If there is an error, have the string “Error” appear in the remainder.
# 列表numb包含整数。 编写代码以用36的余数除以numb中的每个数字填充列表的余数。 例如，第一个元素应为0，因为36/6没有余数。 如果有错误，请在其余部分中显示字符串“ Error”。

numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainder = []
for i in numb:
    if (i == 0):
        remainder.append("Error")
    elif (36 % i):
        remainder.append(36 % i)
    elif (36 % i == 0):
        remainder.append(0)
print(remainder)

# Provided is buggy code, insert a try/except so that the code passes.
# 提供错误的代码，插入try / except，以便代码通过。

lst = [2, 4, 10, 42, 12, 0, 4, 7, 21, 4, 83, 8, 5, 6, 8, 234, 5, 6, 523, 42, 34, 0, 234, 1, 435, 465, 56, 7, 3, 43, 23]

lst_three = []

for num in lst:
    try:
        if 3 % num == 0:
            lst_three.append(num)
    except ZeroDivisionError:
        pass
print(lst_three)

# Write code so that the buggy code provided works using a try/except. When the codes does not work in the try, have it append to the list attempt the string “Error”.
# 编写代码，以便提供的错误代码可以使用try / except进行工作。 如果代码在尝试中不起作用，请将其附加到列表中，然后尝试输入字符串“ Error”。

full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']

attempt = []

for elem in full_lst:
    try:
        attempt.append(elem[1])
    except IndexError:
        attempt.append("Error")
print(attempt)

# The following code tries to append the third element of each list in conts to the new list third_countries. Currently, the code does not work. Add a try/except clause so the code runs without errors, and the string ‘Continent does not have 3 countries’ is appended to countries instead of producing an error.
# 以下代码尝试将续表中每个列表的第三个元素附加到新列表third_countries中。 当前，该代码不起作用。 添加一个try / except子句，使代码运行时没有错误，并且在国家/地区后附加字符串“ Continent没有3个国家/地区”，而不产生错误。

conts = [['Spain', 'France', 'Greece', 'Portugal', 'Romania', 'Germany'], ['USA', 'Mexico', 'Canada'],
         ['Japan', 'China', 'Korea', 'Vietnam', 'Cambodia'],
         ['Argentina', 'Chile', 'Brazil', 'Ecuador', 'Uruguay', 'Venezuela'], ['Australia'],
         ['Zimbabwe', 'Morocco', 'Kenya', 'Ethiopa', 'South Africa'], ['Antarctica']]

third_countries = []

for c in conts:
    try:
        third_countries.append(c[2])
    except IndexError:
        third_countries.append("Continent does not have 3 countries")
print(third_countries)

# The buggy code below prints out the value of the sport in the list sport. Use try/except so that the code will run properly. If the sport is not in the dictionary, ppl_play, add it in with the value of 1.
# 下面的错误代码在列表运动中显示了该运动的价值。 使用try / except，以便代码可以正常运行。 如果运动不在字典ppl_play中，则将其添加为1。

sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]

ppl_play = {"hockey": 4, "soccer": 10, "football": 15, "tennis": 8}

for x in sport:
    try:
        print(ppl_play[x])
    except KeyError:
        ppl_play[x] = 1

# Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so that the code passes. If the key is not there, initialize it in the dictionary and set the value to zero.
# 提供了一个越野车for循环，该循环试图从某些词典中累积一些值。 插入一个try / except，以便代码通过。 如果密钥不存在，请在字典中将其初始化并将其值设置为零。
di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49},
      {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7},
      {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89},
      {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]

total = 0
for diction in di:
    try:
        diction.keys() == "Puppies"
        total = total + diction['Puppies']
    except:
        pass
    if("Puppies" not in diction.keys()):
        diction["Puppies"] = 0

print("Total number of puppies:", total)
