import csv
import operator
import re
from collections import Counter

from tabulate import tabulate

'''
    Program to Count the Frequency of the word from the text file and rank them according to frequecny 
     ---------------------------------------------Part A---------------------------------------------
'''

FILE_NAME = 'shakespeare.txt'
word_count = {}  # create a empty dictionary
word_list = []  # create a empty list for words
count_bigrams = {}  # create a empty dictionary for biagram
bigrams_list = []  # create empty list for biagrams


def get_word_list():
    text_document = ""
    with open(FILE_NAME) as f:
        text_document = f.read()
    final_text = re.findall(r'\b[a-z]{1,}\b', text_document.lower())  # removed punctuation using regular expression
    for s in final_text:
        word_list.append(s)  # add final text to word list
    c = create_dict(word_list)  # create a dictionary form word_list
    top_20 = Counter(c).most_common(20)
    file_write(top_20)


def create_dict(word_list):
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def examples_words():
    bottom_10 = []
    i = 0
    prevValue = 1
    wordCount = 0
    examples = ""
    exampleCount = 0
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        if value != prevValue:
            # create a list to be added to the list
            element = [prevValue, wordCount, examples]
            # re initialize the variables
            prevValue = value
            wordCount = 0
            exampleCount = 0
            examples = ""
            # add the element to the list
            bottom_10.append(element)
            i += 1
            continue

        # break loop to get the 10 entries
        if i == 10:
            break

        # increase word count if the freq is same for the word in the previous iteration also add it to example list
        if value == prevValue:
            wordCount += 1
            if exampleCount != 6:
                if exampleCount != 0:
                    examples = examples + " ," + key
                    exampleCount += 1
                else:
                    examples = key
                    exampleCount += 1
    print("\n")
    print(tabulate(bottom_10, headers=['Frequency', 'Word Count', 'Examples'], tablefmt='rst') + "\n")


def getWordListBigrams():
    for i in range(len(word_list) - 1):
        biagram = word_list[i] + " " + word_list[i + 1]
        bigrams_list.append(biagram)


def print_bigrams():
    print("\n\nQuestion 3:\n")
    #3: A table containing 20 most frequent word-pairs (bigrams). The table contains three columns: rank, word pair and frequency.

    top_20_biagrams = []
    getWordListBigrams()
    create_bigrams_dict()
    i = 0

    # sort the list 'biagrams_count' in descending order and add top 20 elements to 'top_20_biagrams'
    for key, value in sorted(count_bigrams.items(), key=operator.itemgetter(1), reverse=True):
        i += 1
        item = [i, key, value]
        top_20_biagrams.append(item)
        if i == 20:
            break


    print(tabulate(top_20_biagrams, headers=['Rank', 'Word Pair', 'Frequency'], tablefmt='rst') + "\n")


def create_bigrams_dict():
    for bigrams in bigrams_list:
        if bigrams in count_bigrams:
            count_bigrams[bigrams] += 1
        else:
            count_bigrams[bigrams] = 1


def file_write(counts):
    i = 0
    with open("file.csv", "w") as file:
        file.write("Word,Frequency,Rank\n")
        for value, count in counts:
            i = i + 1
            x = (value + ',' + str(count) + ',' + str(i))
            file.write(x + "\n")

        # ----------------Part-A (1) output---------------------------

    with open('file.csv') as csvfile:
        rowReader = csv.reader(csvfile, delimiter=',')
        for values in rowReader:
            print('{2:8} {1:15} {0}'.format(values[0], values[1], values[2]))


def probability(a):
    return word_count[a] / len(word_list)


# calculate the probability for finding word a after word b
def condProd(a, b):
    c = a + " " + b
    return count_bigrams[c] / word_count[a]


def predict(a, b, c):
    prob = 0
    after = []
    prediction = ""

    # put all possible words after c in a list
    for i in range(len(word_list) - 1):
        if word_list[i] == c:
            after.append(word_list[i + 1])

    # check the cumulative probability of all the words in after[]
    for d in after:
        if (prob < (probability(a) * condProd(a, b) * condProd(b, c) * condProd(c, d))):
            prediction = d
            prob = (probability(a) * condProd(a, b) * condProd(b, c) * condProd(c, d))
    return prediction


if __name__ == '__main__':
    print("\n -------------PART A------------------------------------------- \n")
    get_word_list()
    examples_words()
    print_bigrams()

    print("\n\n-----------------PART B--------------------------------------\n")
    # Part B
    # With the frequency counts of the word at our hand we calculate some basic probability estimates.

    print("\nQuestion 1: \n")

    # 1. Calculate the relative frequency (probability estimate) of the words:
    # (a) “the"

    probability_the = word_count['the'] / len(word_list)
    print("The relative frequency of 'the' is: " + str(probability_the))

    # (b) “become"

    probability_become = word_count['become'] / len(word_count)
    print("The relative frequency of 'become' is: " + str(probability_become))

    # (d) “brave"

    probability_brave = word_count['brave'] / len(word_count)
    print("The relative frequency of 'brave' is: " + str(probability_brave))

    # (e) “treason"

    probability_treason = word_count['treason'] / len(word_count)
    print("The relative frequency of 'treason' is: " + str(probability_treason))

    print("\n\nQuestion 2:\n")
    # 2. Calculate the following word conditional probabilities:
    # (a) P(court | The)

    probability_court_given_the = count_bigrams['the count'] / word_count['the']
    print("P(court | The) = " + str(probability_court_given_the))

    # (b) P(word | his)

    probability_word_given_his = count_bigrams['his word'] / word_count['his']
    print("P(word | his) = " + str(probability_word_given_his))

    # (c) P(qualities | rare)

    probability_qualities_given_rare = count_bigrams['rare qualities'] / word_count['rare']
    print("P(qualities | rare) = " + str(probability_qualities_given_rare))

    # (d) P(men | young)

    probability_men_given_young = count_bigrams['young men'] / word_count['young']
    print("P(men | young) = " + str(probability_men_given_young))

    print("\n\nQuestion 3:\n")
    # 3. Calculate the probability:
    # (a) P(have, sent)

    ProbHavSent = count_bigrams['have sent'] / word_count['have']
    print("P(have, sent) = " + str(ProbHavSent))

    PWillLookUpon = probability('will') * condProd('will', 'look') * condProd('look', 'upon')
    print("P(will, look, upon) = " + str(PWillLookUpon))

    # (c) P(I, am, no, baby)

    PIAmNoBaby = probability('i') * condProd('i', 'am') * condProd('am', 'no') * condProd('no', 'baby')
    print("P(I, am, no, baby) = " + str(PIAmNoBaby))

    # (d) P(wherefore, art, thou, Romeo)

    PWheArtThoRom = probability('wherefore') * condProd('wherefore', 'art') * condProd('art', 'thou') * condProd('thou',
                                                                                                                 'romeo')
    print("P(wherefore, art, thou, Romeo) = " + str(PWheArtThoRom))

    print("\n\nQuestion 4:\n")
    # 4. Calculate probabilities in Q3 assuming each word is independent of other words.
    # (a) P(have, sent)

    ProbHavSentIn = probability('have') * probability('sent')
    print("P(have, sent) = " + str(ProbHavSentIn))

    # (b) P(will, look, upon)

    PWillLookUponIn = probability('will') * probability('look') * probability('upon')
    print("P(will, look, upon) = " + str(PWillLookUponIn))

    # (c) P(I, am, no, baby)

    PIAmNoBabyIn = probability('i') * probability('am') * probability('no') * probability('baby')
    print("P(I, am, no, baby) = " + str(PIAmNoBabyIn))

    # (d) P(wherefore, art, thou, Romeo)

    PWheArtThoRomIn = probability('wherefore') * probability('art') * probability('thou') * probability('romeo')
    print("P(wherefore, art, thou, Romeo) = " + str(PWheArtThoRomIn))

    print("\n\nQuestion 5:\n")
    # 5. Find the most probable word to follow this sequence of words:

    # (a) I am no
    print("a. I am no \nI am no " + predict("i", "am", "no"))

    # (b) wherefore art thou
    print("b. wherefore art thou \nwherefore art thou " + predict("wherefore", "art", "thou"))
