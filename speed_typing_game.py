from typing_class import Typing
import random
import time

#author: Love Kildetoft

class Scoreboard:
    """
    class for keeping track of the users highscore in wpm. contains three methods,
    one for checking if the user has managed a new highscore, one for displaying
    the current highscore at the menuscreen and one for clearing the highscore.
    As well as a function which generates a motivational word when the user gets
    the input right. current highscore is stored in a .txt file.
    """
    def check_score(self, score):
        #method for checking if the user has obtained a new highscore.
        #takes a score value as input an overwrites the current highscore
        #if the score superceeds the previous highscore
        scorelist = [] #creates empty list for storing highscore to compare
        highscore = open("highscore.txt", 'r+') #open textfile with read/write permission

        for line in highscore: #reads highscore and appends to list
            line = line.strip() #strip newline characters from list
            scorelist.append(line) #append highscore value to list

        if len(scorelist) == 0 or score > float(scorelist[0]): #checks if scorelist is empty
                                                               #or user has achieved new highscore
            print("New highscore!", score, "wpm")
            highscore.seek(0)
            highscore.write(str(score)) #overwrites the first line in highscore.txt
        else:
            pass

        highscore.close() #close highscore.txt

    def display_score(self):
        #method for displaying highscore on menuscreen
        scorelist = [] #list for temporarily storing highscore
        highscore = open("highscore.txt", 'r') #open highscore.txt with read-only permissions

        for line in highscore: #reads highscore.txt line by line and stores in list
            line = line.strip() #strips list of newline characthers
            scorelist.append(line) #appends highscore to list
        highscore.close() #close highscore.txt

        if len(scorelist) != 0: #checks if scorelist is empty or not
            print("Current highscore:", scorelist[0], "wpm") #prints current highscore
        else:
            pass

    def clear_highscore(self):
        #method for clearing the users highscore
        a = Typing() #initialize Typing object to be able to clear terminal after displaying message
        open("highscore.txt", 'w').close() #opens and overwrites highscore.txt, then close
        print("Highscore cleared!") #displays that the highscore has been cleared
        time.sleep(2) #delay to make the message readable, otherwise it would instantly dissapear
        a.cls() #clear terminal using cls method from Typing

    def be_nice(self):
        #method for generating nice, motivational words to the user. returns a nice thing
        nicelist = ["Splendid!", "Awesome!", "Keep it up!", "Good job!",
                    "You're an excellent typer!", "Go get that highscore!",
                    "Good job!", "Nicely typed!"] #list of nice things

        nicepick = random.randint(0, len(nicelist) - 1) #picks a random index corresponding to
                                                        #a random nice thing
        return nicelist[nicepick] #return a nice word

class TypingGame:
    """
    class containing the main code for two typing-test games,
    one for practicing typing a number of random sentences
    chosen by the user and one for practicing typing a larger
    paragraph. measures the time it takes for the user to type
    correctly as well as the typing speed in words per minute
    by using methods from another class, Typing.
    """
    def sentence_game(self):
        #main function for sentence-typing game.
        typeobject = Typing() #initialize Typing class
        scoreobject = Scoreboard()
        sentence_list = typeobject.read_sentence_file() #read sentence list
                                                        #see Typing class
        timelist = [] #initializes two list to contain times and wpm of user
        wpm_list = []

        playgame = True #setting up main game boolean
        while playgame: #initialize loop
            errorcount = 0

            typeobject.cls() #clear terminal

            trials = typeobject.take_tries() #take input number of sentences
                                             #the user would like to practice
            typeobject.cls() #clear terminal again

            print("Get ready") #tell the user to get ready and counts down from
            time.sleep(1) #3, then starts the game, delay 1 second
            typeobject.countdown() #runs countdown, see Typing class

            typeobject.cls() #clear terminal again

            for i in range(trials): #sets up loop for handling number of
                                    #tries
                sentence = typeobject.pick_sentence(sentence_list) #picks a random sentence
                print("Please type:") #asks user to type
                print(sentence) #displays sentence to be typed

                type = True #set up main boolean for handling incorrect input

                while type: #main loop for typing, handles incorrect inpup
                    user = typeobject.speedtype_timing() #takes input and times it
                    if user[0] != sentence: #checks correctness of input
                        print("Try again")
                        errorcount += 1
                    else: #breaks the loop if input matches randomly chosen sentence
                        type = False

                measure_wpm = typeobject.words_per_minute(user[0], user[1]) #returns the words/minute (see Typing)
                                                                            #from measured time and input string
                timelist.append(user[1]) #adds time for each try to list
                wpm_list.append(measure_wpm) #adds wpm for each try

                benice = scoreobject.be_nice()
                print(benice)
                time.sleep(1)

                typeobject.cls() #clears terminal for each round

            average_time = sum(timelist)/len(timelist) #calculate average time
            average_wpm = sum(wpm_list)/len(wpm_list) #calculate average wpm

            scoreobject.check_score(average_wpm) #check if the user achieved a new highscore

            print("Your average typing time was:", average_time, "seconds") #prints average typing time
            print("With an average typing speed of:", average_wpm, "words per minute") #prints average wpm
            print("You had", errorcount, "errors")
            print("Play again? y/n") #asks if user would like to play again

            again = True #set up boolean for playing again
            while again: #while loop handling wrongly formatted input from user and playing again
                play_again = str(input()) #takes input, asks for y/n
                if play_again == "y": #breaks loop if user answered yes
                    again = False
                elif play_again == "n": #breaks both main game loop and play again loop if user answered no
                    print("Bye!")
                    time.sleep(1)
                    again = False
                    playgame = False
                    typeobject.cls()
                else: #checks for errors in input
                    print("You can only pick y/n. Try again!")

    def paragraph_game(self):
        #main function for paragraph-typing game
        typeobject = Typing() #initialize Typing class
        scoreobject = Scoreboard()
        paragraph_list = typeobject.read_paragraph_file() #reads paragraphs to list

        playgame = True #set up main game boolean

        while playgame: #set main game loop
            typeobject.cls() #clear terminal

            print("Get ready") #tell the user to get ready and counts down from
            time.sleep(1) #3, delay 1 second
            typeobject.countdown() #runs countdown, see Typing

            typeobject.cls() #clears terminal again

            paragraph = typeobject.pick_sentence(paragraph_list) #picks a random paragraph
            print("Please type:") #asks user to type
            print(paragraph) #displays paragraph to be typed

            type = True #set up main boolean for handling incorrect input
            while type: #loop for handling incorrect input
                user = typeobject.speedtype_timing() #takes input and times the user (see Typing)
                if user[0] != paragraph: #checks if input is correct, otherwise loop continues
                    print("Try again")
                else: #breaks loop if input is correct
                    type = False

            benice = scoreobject.be_nice()
            print(benice)
            time.sleep(1)

            typeobject.cls() #clear terminal

            measure_wpm = typeobject.words_per_minute(user[0], user[1]) #measures total wpm of user, see typing

            scoreobject.check_score(measure_wpm) #checks if wpm is new highscore

            print("Your total typing time was", user[1], "seconds =", user[1]*(1/60), "minutes") #prints total typing time in seconds
                                                                                                 #and minutes by converting
            print("Your typing speed was:", measure_wpm, "words per minute") #prints calculated yping speed of the user in wpm
            print("Play again? y/n") #asks if user would like to play again

            again = True
            while again:
                play_again = str(input()) #same methodology as in sentence_game, identical code. see sentence_game for detailed
                                          #comments
                if play_again == "y":
                    again = False
                elif play_again == "n":
                    print("Bye!")
                    time.sleep(1)
                    again = False
                    playgame = False
                    typeobject.cls()
                else:
                    print("You can only pick y/n. Try again!")
