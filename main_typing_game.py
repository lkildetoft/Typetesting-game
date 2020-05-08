from speed_typing_game import *
from typing_class import *

#author: Love Kildetoft

def mainloop():
    """
    main function comprising the whole typing game. uses the class TypingGame created by yours
    truly. offers a simple menu screen and initializes the different game types depending on the
    user input.
    """
    maingame = TypingGame() #initialize typinggame object.
    highscore = Scoreboard() #initialize scoreboard object
    typing = Typing() #initialize typing object

    typing.cls()

    menuscreen = True #set up  boolean for handling user choice.
    while menuscreen: #set up main loop for menu screen.
        print("Welcome!")
        print("What would you like to do today?")
        print("1. Practice typing a number of shorter sentences")
        print("2. Practice typing a larger paragraph")
        print("3. Clear highscore")
        print("4. Exit the game")
        highscore.display_score()

        try_input = True #set up boolean for handling incorrect menu choices
        while try_input: #loop which handles incorrect menu choices
            user_input = input()
            if user_input == "1":
                try_input = False
                maingame.sentence_game()
            elif user_input == "2":
                try_input = False
                maingame.paragraph_game()
            elif user_input == "3":
                highscore.clear_highscore()
                try_input = False
            elif user_input == "4":
                print("Bye!")
                try_input = False
                menuscreen = False
            elif user_input == "42":
                for i in range(10):
                    print("THE ANSWER TO LIFE, THE UNIVERSE AND EVERYTHING")
                    time.sleep(0.5)
                print("The programmer put this in for YOU")
                time.sleep(5)
                print("Also your highscore is now gone")
                highscore.clear_highscore()
                try_input = False
            else:
                print("You can only input 1, 2, 3 or 4")

if __name__ == "__main__":
    mainloop()
