import random
import time
import os

#author: Love Kildetoft

class Typing:
    """
    class for handling reading, inputing and randomly picking sentences
    for a type-testing game. contains methods for reading files,
    timing and taking user input, and calculating typing speed in words-
    per-minute.
    """
    def read_sentence_file(self):
        #function for reading the file containing practice sentences
        #returns list of sentences
        sentence_list = [] #create empty list for storing the sentences from the document
        sentence_file = open("sentences.txt", "r") #opening the file and assigning it variable

        for line in sentence_file: #reading the file line by line
            line = line.strip() #removing \n (newline) characters from each line
            sentence_list.append(line) #appending lines to list

        return sentence_list

    def read_paragraph_file(self):
        #function for reading the file containing practice sentences
        #essentially identical to the read_sentence_file method
        paragraph_list = []
        paragraph_file = open("paragraphs.txt", "r")

        for line in paragraph_file:
            line = line.strip()
            paragraph_list.append(line)

        paragraph_list = [a for a in paragraph_list if a != ''] #removing superfluous elements in list

        return paragraph_list

    def pick_sentence(self, list_of_typing):
        #picks a random sentence from an input list.
        #returns sentence at generated index
        get_sentence = random.randint(0, len(list_of_typing) - 1) #generate random number in the
                                                              #range of the input list
        return list_of_typing[get_sentence]

    def take_tries(self):
        #method for taking the number of sentences the user would like to practice.
        #handles wrongly formatted input, only accepts integers. returns an integer
        try_input = True #setting up boolean for handling wrongly formatted input

        while try_input:
            #take input
            tries = input("How many times would you like to test your typing? Input an integer")
            if not tries.isdigit(): #checks if input is integer by using built in isdigit() method.
                print("You must input an integer. Try again!") #prints error message
            else:
                try_input = False #breaks the loop

        return int(tries)

    def speedtype_timing(self):
        #method for timing the user's typing.
        #takes input and returns a list of the input and the time it took
        start = time.time() #takes time at start of input
        user_input = str(input()) #take input string
        end = time.time() #takes time at end of input

        timing = [user_input, end - start] #list of input and the time difference
                                           #between start and end
        return timing

    def words_per_minute(self, words, time):
        #method for measuring words per minute from a string of words and the time it took
        #to write the list in seconds. returns corresponding words-per-minute
        wordlist = words.split() #splits input string of words into list of words
        minutes = time*(1/60) #converts input time in seconds to minutes
        wpm = len(wordlist)/minutes #calculate words/minute

        return wpm

    def countdown(self):
        #method for generating 3 second countdown timer, to be displayed at start of
        #each game.
        for i in range(0, 3):
            print(3 - i)
            time.sleep(1)

    def cls(self):
        #method for clearing the terminal. checks if os is windows or unix and corrects
        #accordingly.
        os.system('cls' if os.name=='nt' else 'clear')
