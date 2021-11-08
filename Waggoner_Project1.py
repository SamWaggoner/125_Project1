# File: Project1_COS.py
# Author: Sam Waggoner
# Date: 11/09/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Finds sentiments of individial words or entire files of words, or calculates
# the word with the highest and lowest sentiments, based off movie reviews.
# Collaboration:
# I did not collaborate with anyone. VJ helped me use his test files.

# This program:
# - does not consider individual numbers in reviews when finding ratings
# - does not consider any characters, including: ,?.!;:'\"1234567890-=_+`~{@}#|$%^&*()[]<>/\
# - does not discriminate with capitalization
# - DOES discriminate against suffixes, prefixes, and similar cases: roughly would not be considered
#       for searchword "rough", highly would not be included for searchword "hi".

# takes a file name and returns a list of tuples comprising each word and rating as (word,rating)
def ratings_makewordlist(filename):
    reviews = open(filename, "r")
    wordlist = []
    # split each line of the review file by spaces, assign rating to the first character
    for line in reviews:
        rating = line[0]
        linelist = line.split()

        # delete punctuation, make lowercase, and delete spaces (empty indexes where symbols/numbers were since they were standalone)
        for index in range(len(linelist)):
            unstrippedword = linelist[index]
            unstrippedword = unstrippedword.strip(",?.!;:'\"1234567890-=_+`~{@}#|$%^&*()[]<>/\\")
            linelist[index] = unstrippedword.lower()
        while "" in linelist:
            linelist.remove("")

        for index in range(len(linelist)):
            wordlist.append((linelist[index],rating))
    reviews.close()
    return wordlist

# main structure for task 1, returns a word and its average score in the reviews file
def task1(word):
    filename = input("What is the name of the file you want to check? ")
    wordlist = ratings_makewordlist(filename)
    counter = 0
    scoretotal = 0

    # in the file, if the input word is found, add the rating to a total and add 1 to a counter
    for index in range(len(wordlist)):
        if wordlist[index][0] == word:
            scoretotal += int(wordlist[index][1])
            counter += 1

    if counter != 0:
        average = (scoretotal/counter)
        return(word,average,counter)
    if counter == 0:
        return("error")
        

# takes a word and the name of the reviews file, returns an average score for that word
def reviews_task1(word,reviewfilename):
    # gets wordlist for reviews file
    wordlist = ratings_makewordlist(reviewfilename)

    # if input word is in wordlist, adds its score to total and adds 1 to counter
    counter = 0
    scoretotal = 0
    for index in range(len(wordlist)):
        if wordlist[index][0] == word:
            scoretotal += int(wordlist[index][1])
            counter += 1

    if counter != 0:
        average = (scoretotal/counter)
        return(average)
    if counter == 0:
        return("error")
    
# returns a list of all of the words in a file
def normal_makewordslist(filename):
    wordfile = open(filename, "r")
    wordlist = []
    for eachline in wordfile:
        linelist = eachline.split()

        # delete punctuation, numbers, and symbols, make lowercase, 
        for index in range(len(linelist)):
            unstrippedword = linelist[index]
            unstrippedword = unstrippedword.strip(",?.!;:'\"1234567890-=_+`~{@}#|$%^&*()[]<>/\\")
            linelist[index] = unstrippedword.lower()
        # and delete spaces (empty indexes where symbols/numbers/punctuation were since they were standalone)
        while "" in linelist:
            linelist.remove("")
            
        for index in range(len(linelist)):
            wordlist.append(linelist[index])
    wordfile.close()
    return wordlist

# main structure for task 2, returns average
def task2():
    wordfilename = input("What is the name of the file you want to check? ")
    reviewfilename = input("What is the name of the reviews file to which you want to refer? ")
    # list of all the words in the file: checkwordlist
    checkwordlist = normal_makewordslist(wordfilename)

    total = 0
    numwordsinfile = 0
    # find the score of each word, add it to a runnng total, for each word found in the document add one to a count
    for i in range(len(checkwordlist)):
        score = reviews_task1(checkwordlist[i],reviewfilename)
        if score != "error":
            total += score
            numwordsinfile += 1

    if numwordsinfile == 0:
        return("error")
    else:
        overall_avg = total/numwordsinfile
        return overall_avg

# structure for task 3, returns the maximum and minimum sentiments and their words
def task3():
    wordfilename = input("What is the name of the file you want to check? ")
    reviewfilename = input("What is the name of the reviews file to which you want to refer? ")
    # list of all the words in the file: checkwordlist
    checkwordlist = normal_makewordslist(wordfilename)
    maxscore = 1
    minscore = 4
    if len(checkwordlist) == 0:
        return("error")

    # find the score of each word, if it is more extreme than the current min/max score, update the min/max score
    else:
        for index in range(0,(len(checkwordlist))):
            score = reviews_task1(checkwordlist[index],reviewfilename)
            if score != "error":
                if score < minscore:
                    minscore = score
                    minword = checkwordlist[index]
                if score > maxscore:
                    maxscore = score
                    maxword = checkwordlist[index]

        return(wordfilename,minword,minscore,maxword,maxscore)






# Menu:

"""
Info:
Rating system is out of 5.
An insult has an average sentiment of less than 
1.75, while a compliment has an average sentiment of more than 2.25.
"""
def main():
    print("What task would you like to run?")
    print("Task 1: Calculate the sentiment score of a single word in a file")
    print("Task 2: Calculate the average score of all the words in a file")
    print("Task 3: Find the highest and lowest scoring words in a file")
    print("Task 4: Quit")
    choice = int(input("Enter the number of the task you would like to run: "))

    if choice == 1:
        word = input("What is the word you would like to check? ")
        result = task1(word)
        if result != "error":
            print("The word \""+str(result[0])+"\""+" appers "+str(result[2])+" times.")
            print("The average sentiment for "+"\""+str(result[0])+"\""+" is "+str(result[1])+".\n")
        if result == "error":
            print("There were no instances of your word in the reviews provided.\n")

    if choice == 2:
        avg = task2()
        if avg == "error":
            print("There are no words in the file you would like to check.\n")
        else:
            if avg > 2.25:
                print("The average word score for your whole file was "+str(avg)+"."+" This is likely a complement.\n")
            if avg < 1.75:
                print("The average word score for your whole file was "+str(avg)+"."+" This is likely an insult.\n")
            if avg <= 2.25 and avg >= 1.75:
                print("The average word score for your whole file was "+str(avg)+"."+" This is likely a neutral statement.\n")

    if choice == 3:
        result = task3()
        if result == "error":
            print("There are no words in the file you would like to check.\n")
        else:
            print("The most positive word in "+str(result[0])+" was "+str(result[3])+" with a score of "+str(result[4])+".")
            print("The most negative word in "+str(result[0])+" was "+str(result[1])+" with a score of "+str(result[2])+".\n")


    while choice != 4:
        print("What task would you like to run?")
        print("Task 1: Calculate the sentiment score of a single word in a file")
        print("Task 2: Calculate the average score of all the words in a file")
        print("Task 3: Find the highest and lowest scoring words in a file")
        print("Task 4: Quit")
        choice = int(input("Enter the number of the task you would like to run: "))

        if choice == 1:
            word = input("What is the word you would like to check? ")
            result = task1(word)
            if result != "error":
                print("The word \""+str(result[0])+"\""+" appers "+str(result[2])+" times.")
                print("The average sentiment for "+"\""+str(result[0])+"\""+" is "+str(result[1])+".\n")
            if result == "error":
                print("There were no instances of your word in the reviews provided.\n")

        if choice == 2:
            avg = task2()
            if avg == "error":
                print("There are no words in the file you would like to check.\n")
            else:
                if avg > 2.25:
                    print("The average word score for your whole file was "+str(avg)+"."+" This is likely a complement.\n")
                if avg < 1.75:
                    print("The average word score for your whole file was "+str(avg)+"."+" This is likely an insult.\n")
                if avg <= 2.25 and avg >= 1.75:
                    print("The average word score for your whole file was "+str(avg)+"."+" This is likely a neutral statement.\n")

        if choice == 3:
            result = task3()
            if result == "error":
                print("There are no words in the file you would like to check.\n")
            else:
                print("The most positive word in "+str(result[0])+" was "+str(result[3])+" with a score of "+str(result[4])+".")
                print("The most negative word in "+str(result[0])+" was "+str(result[1])+" with a score of "+str(result[2])+".\n")

main()