# coding:utf-8
# File Name：     course_4_project
# Description :
# Author :       micro
# Date：          2019/10/30
import random
VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'


# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    prizeMoney = 0
    prizes = []

    def __init__(self, name):
        self.name = name

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return "%s (%s)" % (self.name, self.prize)


# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guesse):
        input(
            "{%s} has ${%s}\n"
            "Category: {%s}\n"
            "Phrase:  {%s}\n"
            "Guessed: {%s}\n"
            "Guess a letter, phrase, or type 'exit' or 'pass':\n") % (
            self.name, self.prizeMoney, category, obscuredPhrase, guesse)
        return ("%s") % (guesse)


# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"

    def __init__(self, difficulty):
        self.difficulty = difficulty

    def smartCoinFlip(self):
        random_num = random.randint(1, 10)
