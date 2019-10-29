# coding:utf-8
# File Name：     course_4_assessment_2
# Description :
# Author :       micro
# Date：          2019/10/29
# The class, Pokemon, is provided below and describes a Pokemon and its leveling and evolving characteristics. An instance of the class is one pokemon that you create.
#
# Grass_Pokemon is a subclass that inherits from Pokemon but changes some aspects, for instance, the boost values are different.
#
# For the subclass Grass_Pokemon, add another method called action that returns the string "[name of pokemon] knows a lot of different moves!". Create an instance of this class with the name as "Belle". Assign this instance to the variable p1.
# 下面提供了神奇宝贝类，描述了神奇宝贝及其级别和演变特性。 该类的一个实例是您创建的一个神奇宝贝。
#
# Grass_Pokemon是一个继承自Pokemon的子类，但是会更改某些方面，例如，boost值不同。
#
# 对于子类Grass_Pokemon，添加另一个名为action的方法，该方法返回字符串“ [pokemon的名称]知道很多不同的动作！”。 创建一个名为“ Belle”的此类的实例。 将此实例分配给变量p1。
class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)


class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return "%s knows a lot of different moves!" % self.name


p1 = Grass_Pokemon("Belle")
print(p1.action())
# Modify the Grass_Pokemon subclass so that the attack strength for Grass_Pokemon instances does not change until they reach level 10. At level 10 and up, their attack strength should increase by the attack_boost amount when they are trained.
#
# To test, create an instance of the class with the name as "Bulby". Assign the instance to the variable p2. Create another instance of the Grass_Pokemon class with the name set to "Pika" and assign that instance to the variable p3. Then, use Grass_Pokemon methods to train the p3 Grass_Pokemon instance until it reaches at least level 10.
# 修改Grass_Pokemon子类，以使Grass_Pokemon实例的攻击强度在达到第10级之前不会改变。在第10级及更高级别上，训练它们的攻击强度应增加Attack_boost数量。
#
# 为了进行测试，创建一个名为“ Bulby”的类的实例。 将实例分配给变量p2。 创建名称设置为“ Pika”的Grass_Pokemon类的另一个实例，并将该实例分配给变量p3。 然后，使用Grass_Pokemon方法训练p3 Grass_Pokemon实例，直到至少达到10级。

p2 = Grass_Pokemon("Bulby")
p3 = Grass_Pokemon("Pika")
p3.train()
p3.train()
p3.train()
p3.train()
p3.train()

print(p3.level)


# Along with the Pokemon parent class, we have also provided several subclasses. Write another method in the parent class that will be inherited by the subclasses. Call it opponent. It should return which type of pokemon the current type is weak and strong against, as a tuple.
#
# Grass is weak against Fire and strong against Water
# Ghost is weak against Dark and strong against Psychic
# Fire is weak against Water and strong against Grass
# Flying is weak against Electric and strong against Fighting
# For example, if the p_type of the subclass is 'Grass', .opponent() should return the tuple ('Fire', 'Water')
# 除了Pokemon父类，我们还提供了几个子类。 在父类中编写另一个将由子类继承的方法。 称它为对手。 它应该以元组的形式返回当前类型的弱小宠物和强宠物小精灵。
#
# 草对火弱，对水强
# 幽灵对黑暗较弱，对精神较弱
# 火对水弱，对草强
# 飞行对电子弱，对战斗强
# 例如，如果子类的p_type为'Grass'，则.opponent（）应返回元组（'Fire'，'Water'）
class Pokemon():
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

    def opponent(self):
        if self.p_type == "Grass":
            return ('Fire', 'Water')
        elif self.p_type == "Ghost":
            return ('Dark', 'Psychic')
        elif self.p_type == "Ghost":
            return ('Dark', 'Psychic')
        elif self.p_type == "Fire":
            return ('Water', 'Grass')
        elif self.p_type == "Flying":
            return ('Electric', 'Fighting')


class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12


class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def update(self):
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3


class Fire_Pokemon(Pokemon):
    p_type = "Fire"


class Flying_Pokemon(Pokemon):
    p_type = "Flying"
