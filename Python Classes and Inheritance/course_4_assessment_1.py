# coding:utf-8
# File Name：     course_4_assessment_1
# Description :
# Author :       micro
# Date：          2019/10/29
# Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price. Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0.
class Bike:
    def __init__(self, str, float):
        self.color = str
        self.price = float


testOne = Bike("blue", 89.99)
testTwo = Bike("purple", 25.0)


# Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples. The constructor should initialize two instance variables: apple_color and apple_quantity. Write a class method called increase that increases the quantity by 1 each time it is invoked. You should also write a __str__ method for this class that returns a string of the format: "A basket of [quantity goes here] [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket of 50 blue apples." (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)

# 创建一个名为AppleBasket的类，其构造函数接受两个输入：代表颜色的字符串和代表苹果数量的数字。 构造函数应初始化两个实例变量：apple_color和apple_quantity。 编写一个称为增加的类方法，该方法在每次调用时将其数量增加1。 您还应该为此类编写一个__str__方法，该方法返回以下格式的字符串：“一篮子[数量在这里] [颜色在这里]苹果。” 例如 “一篮子四个红苹果。” 或“一篮子50个蓝色苹果”。 （编写一些创建实例并将变量赋值的测试代码可以帮助您解决此问题！）

class AppleBasket:
    def __init__(self, apple_color, apple_quantity):
        self.apple_color = apple_color
        self.apple_quantity = apple_quantity

    def increase(self):
        self.apple_quantity += 1

    def __str__(self):
        return "A basket of %s %s apples." % (self.apple_quantity, self.apple_color)


# Define a class called BankAccount that accepts the name you want associated with your bank account in a string, and an integer that represents the amount of money in the account. The constructor should initialize two instance variables from those inputs: name and amt. Add a string method so that when you print an instance of BankAccount, you see "Your account, [name goes here], has [start_amt goes here] dollars." Create an instance of this class with "Bob" as the name and 100 as the amount. Save this to the variable t1.

# 定义一个名为BankAccount的类，该类以字符串形式接受要与银行帐户关联的名称，以及一个表示该帐户中金额的整数。 构造函数应从这些输入初始化两个实例变量：name和amt。 添加一个字符串方法，以便当您打印BankAccount的实例时，看到“您的帐户[名称在此处]有[start_amt在此处]美元”。 创建一个此类的实例，名称为“ Bob”，数量为100。 将其保存到变量t1。
class BankAccount:
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def __str__(self):
        return "Your account, %s, has %s dollars." % (self.name, self.amt)

t1 = BankAccount("Bob",100)