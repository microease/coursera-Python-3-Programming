# coding:utf8
# Author :       huxiaoyi
# Date：         2019-04-18
# Time：         23:42

# We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
#
# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.
#
# To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)
#
# punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
#
#
def strip_punctuation(oldS):
    for i in punctuation_chars:
        oldS = str(oldS).replace('%s' % i, '')
    return oldS


#
# print(strip_punctuation('#Amazing'))
# Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents a one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurances there are of positive words in the text.
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# list of negative words to use

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(oldS):
    for i in punctuation_chars:
        oldS = str(oldS).replace('%s' % i, '')
    return oldS


def get_pos(str):
    str = strip_punctuation(str).split()
    j = 0
    for i in str:
        if i in positive_words:
            j += 1
    return j


def get_neg(str):
    str = strip_punctuation(str).split()
    k = 0
    for i in str:
        if i in negative_words:
            k += 1
    return k


def run(file):
    csvFile = open(file, 'r')
    lines = csvFile.readlines()
    # print(lines[0])
    lines = lines[1:]
    neg_count = []
    pos_count = []
    wordList = []
    for i in lines:
        i = i.strip()
        i = i.split(",")[0]
        wordList.append(i)
    for i in wordList:
        neg_count.append(get_neg(i))
        pos_count.append(get_pos(i))
    res = ['retweet_count,reply_count,pos_count,neg_count,score']
    # 删除推文
    res = []
    for i in lines:
        i = i.strip()
        i = i.split(",")[1:]
        res.append(i)
    temp = []
    for i in res:
        i = list(map(int, i))
        temp.append(i)
    res = temp
    for i in range(len(res)):
        res[i].append(pos_count[i])
        res[i].append(neg_count[i])
        res[i].append(pos_count[i] - neg_count[i])
        # print(res[i])
    temp = []
    for i in res:
        temp.append(','.join('%s' %id for id in i))
    res = temp
    # res[i] = str(res[i]) +str(pos_count[i]) + str(neg_count[i]) + str(pos_count[i] + neg_count[i])
    res.insert(0, "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    print(res)
    res = '\n'.join('%s' % id for id in res)
    with open("resulting_data.csv", 'w') as csvFile:
        write = csvFile.write(res)


if __name__ == '__main__':
    run('project_twitter_data.csv')
