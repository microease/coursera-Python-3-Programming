# coding:utf-8
# File Name：     course_4_assessment_3
# Description :
# Author :       micro
# Date：          2019/10/30
# The function mySum is supposed to return the sum of a list of numbers (and 0 if that list is empty), but it has one or more errors in it. Use this space to write test cases to determine what errors there are. You will be using this information to answer the next set of multiple choice questions.
# 函数mySum应该返回一个数字列表的总和（如果该列表为空，则返回0），但是其中包含一个或多个错误。 使用此空间编写测试用例，以确定存在哪些错误。 您将使用此信息来回答下一组选择题。
import test


def mySum(list):
    if len(list) > 0:
        res = 0
        for i in list:
            res += i
        return res
    else:
        return 0


# The class Student is supposed to accept two arguments in its constructor:
# A name string
# An optional integer representing the number of years the student has been at Michigan (default:1)
# Every student has three instance variables:
# self.name (set to the name provided)
# self.years_UM (set to the number of years the student has been at Michigan)
# self.knowledge (initialized to 0)
# There are three methods:
# .study() should increase self.knowledge by 1 and return None
# .getKnowledge() should return the value of self.knowledge
# .year_at_umich() should return the value of self.years_UM
# There are one or more errors in the class. Use this space to write test cases to determine what errors there are. You will be using this information to answer the next set of multiple choice questions.
# 学生类应该在其构造函数中接受两个参数：
# 名称字符串
# 可选整数，表示学生在密歇根州的年限（默认值：1）
# 每个学生都有三个实例变量：
# self.name（设置为提供的名称）
# self.years_UM（设置为学生在密歇根州的学习年限）
# self.knowledge（初始化为0）
# 有三种方法：
# .study（）应该将self.knowledge增加1并返回None
# .getKnowledge（）应该返回self.knowledge的值
# .year_at_umich（）应该返回self.years_UM的值
# 该类中存在一个或多个错误。 使用此空间编写测试用例，以确定存在哪些错误。 您将使用此信息来回答下一组选择题。
class Student:
    def __init__(self, name, year_UM, knowledge):
        self.name = name
        self.year_UM = year_UM
        self.knowledge = knowledge

    def study(self):
        self.knowledge += 1
        return None

    def getKnowledge(self):
        return self.knowledge

    def year_at_umich(self):
        return self.year_UM
