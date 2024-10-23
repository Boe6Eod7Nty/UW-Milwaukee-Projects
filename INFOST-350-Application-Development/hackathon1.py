# We do X with Y by Z
#    what action is performed, X
#    who they perform for, Y
#    how that is achieved, Z

# We are Team 4window, we do hackathons
# For our friends in IST - 350
# by using python with libraries

import os  # used to clear console for pretty UI
import random  # select random from lists
import time  # enables waiting for a set time

# Jason Lines
print("Welcome to gaming")


####################### Rock Paper Scissors
def gameRPS():  # Start function
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("You are playing Rock Paper Scissors")
    ## get user input on their hand throw
    handform = input("Rock Paper or Scissors? ").lower()
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'

    #Ben Lines
    comp = ''
    ai_rand = random.randrange(1, 3)  #random number from 1-3

    # convert random number to RPS string
    if ai_rand == 1:
        comp = 'rock'
    elif ai_rand == 2:
        comp = 'paper'
    elif ai_rand == 3:
        comp = 'scissors'
    else:
        print('ERROR')

    print('computer played ' + comp)
    print('user played ' + handform)

    #Noura Lines
    if (handform == rock
            and comp == scissors) or (handform == scissors
                                      and comp == paper) or (handform == paper
                                                             and comp == rock):
        print("YOU WIN!")
    elif handform == rock and comp == rock or handform == scissors and comp == scissors or handform == paper and comp == paper:
        print("IT'S A TIE!")
    elif handform == rock and comp == paper or handform == scissors and comp == rock or handform == paper and comp == scissors:
        print("YOU LOSE!")


####################### Higher or Lower
def gameHOL():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    hiddenNumber = random.randrange(1, 10)
    print("Welcome to 'Higher or Lower'!")
    playerNumber = input("Guess a number between 1 & 10: ")
    correctGuess = False

    playingGuessNumber = True  #set while-loop's exit variable
    while playingGuessNumber:
        if int(playerNumber) == hiddenNumber:
            playingGuessNumber = False  #Exit while loop when guess matches
            correctGuess = True
        elif int(playerNumber) > hiddenNumber:
            print("Too high, try again!")
        elif int(playerNumber) < hiddenNumber:
            print("Too low, try again!")
        else:
            print("Unknown Error, try again")
        if not correctGuess:  #if another guess needed;
            playerNumber = input("Guess another number: ")
    #end while
    if correctGuess:  #while loop ended, print win condition and ends function
        print("Correct Guess!")


####################### Dice roll
def gameDICE():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Welcome to dice!")
    diceQuantity = input("How many dice would you like to roll? ")
    diceResult = 0
    print("Rolling dice...")
    time.sleep(1)  #delay makes it look like it's thinking
    for i in range(1, int(diceQuantity) + 1):  # from 1-X, X = user dice number
        diceResult += random.randrange(
            1, 6)  # random dice roll, add it to current total
    print("Finished Rolling dice")
    print("Total rolled: " + str(diceResult))


#############################################
# End of function definitions, Start functional logic:
programActive = True  # variable tells the code if it should loop again,
#    or exit if the user entered 'q'
while programActive:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Please choose a game to play")
    print("Available games:")
    print(" 1 - Rock, Paper, Scissors")
    print(" 2 - Tic-Tac-Toe")
    print(" 3 - Higher or Lower")
    print(" 4 - Dice Roll")
    gameChoice = input(
        "Which game mode would you like to play? (number, or q to quit) ")
    if gameChoice == 'q':
        programActive = False  # exits program
    elif gameChoice == '1':
        gameRPS()  # runs the rock paper scissors game function
        time.sleep(2)  # waits for 2 seconds, helps user see end of game
    elif gameChoice == '2':
        import tictactoe  # runs the Tic Tac Toe py file
        time.sleep(2)
    elif gameChoice == '3':
        gameHOL()  # runs the Guess the Number game function
        time.sleep(2)
    elif gameChoice == '4':
        gameDICE()
        time.sleep(2)
    else:
        print("Invalid game choice, please try again")

print("Thanks for playing!")
