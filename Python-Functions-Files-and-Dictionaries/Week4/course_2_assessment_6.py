# coding:utf-8
# Author :     microease
# Date :       2019/4/17
# Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
# def sublist(num_list):
#     res = []
#     for i in num_list:
#         if i !=5:
#             res.append(i)
#         elif i ==5:
#             break
#     return res
#
#
# a = sublist([1, 2, 3, 4, 5, 6, 7, 8])
# print(a)

# Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.
#
# def check_nums(num_list):
#     res = []
#     for i in num_list:
#         if i !=7:
#             res.append(i)
#         elif i ==7:
#             break
#     return res
#
#
# a = check_nums([1, 2, 3, 4, 5, 6, 7, 8])
# print(a)

# Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
# def sublist(str_list):
#     res = []
#     for i in str_list:
#         if i !="STOP":
#             res.append(i)
#         elif i =="STOP":
#             break
#     return res

# Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.
# def stop_at_z(str_list):
#     res = []
#     for i in str_list:
#         if i == "z":
#             break
#         else:
#             res.append(i)
#     return res

# Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.


# sum1 = 0
#
# lst = [65, 78, 21, 33]
#
# for x in lst:
#     sum1 = sum1 + x
#
# sum2 = 0
#
# i = 0
# while i < len(lst):
#     sum2 += lst[i]
#     i += 1
# print(sum2)

# Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing

def beginning(list):
    res = []
    for i in list:
        if i == 'bye':
            break
        else:
            res.append(i)
    if len(res) >= 10:
        return res[0:10]
    else:
        return res[0:len(res)]


print(beginning(
    ['water', 'phone', 'home', 'chapstick', 'market', 'headphones', 'bye', 'stickie notes', 'snapchat', 'facebook',
     'social media']))
