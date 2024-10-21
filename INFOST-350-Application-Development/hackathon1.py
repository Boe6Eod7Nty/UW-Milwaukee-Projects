import random
import time

# Jason Lines 
print("Welcome to gaming")

####################### Rock Paper Scissors
def gameRPS(): # Start function
    print("You are playing Rock Paper Scissors")
    ## get user input on their hand throw
    handform = input("Rock Paper or Scissors? ").lower()
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'

    #Ben Lines
    comp = ''
    ai_rand = random.randrange(1,3) #random number from 1-3

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
    if (handform == rock and comp == scissors) or (handform == scissors and comp == paper) or (handform == paper and comp == rock):
         print("YOU WIN!")
    elif handform == rock and comp == rock or handform == scissors and comp == scissors or handform == paper and comp == paper:
        print("IT'S A TIE!")
    elif handform == rock and comp == paper or handform == scissors and comp == rock or handform == paper and comp == scissors:
        print("YOU LOSE!")


####################### TIC-TAC-TOE
def gameTTT():
    print("You are playing Tic-Tac-Toe")
    board = "\n1|2|3\n4|5|6\n7|8|9"
    print(board)

    spots = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

    player1move=int(input("It's your turn to choose a spot: "))

    i = 1
    while i<=9 and player1move <= 9 and player1move >=1 :
        i+=1

        # prompt user for another turn

        # update spots variable to 'x' or 'o'

        board =  "\n"+spots[1]+"|"+spots[2]+"|"+spots[3]\
                +"\n"+spots[4]+"|"+spots[5]+"|"+spots[6]\
                +"\n"+spots[7]+"|"+spots[8]+"|"+spots[9]
        print(board)
    else:
        print("invalid number, try again")


####################### Higher or Lower
def gameHOL():
    hiddenNumber = random.randrange(1,10)
    print("You are playing 'Higher or Lower'!")
    playerNumber = input("Guess a number between 1 & 10: ")
    correctGuess = False

    playingGuessNumber = True #set while-loop's exit variable
    while playingGuessNumber:
        if int(playerNumber) == hiddenNumber:
            playingGuessNumber = False #Exit while loop when guess matches
            correctGuess = True
        elif int(playerNumber) > hiddenNumber:
            print("Too high, try again!")
        elif int(playerNumber) < hiddenNumber:
            print("Too low, try again!")
        else:
            print("Unknown Error, try again")
        if not correctGuess: #if another guess needed;
            playerNumber = input("Guess another number: ")
    #end while
    if correctGuess: #while loop ended, print win condition and ends function
        print("Correct Guess!")


####################### Dice roll
def gameDICE():
    print("Welcome to dice!")
    diceQuantity = input("How many dice would you like to roll? ")
    diceResult = 0
    print("Rolling dice...")
    time.sleep(1) #delay makes it look like it's thinking
    for i in range(1, int(diceQuantity) + 1): # from 1-X, X = user dice number
        diceResult += random.randrange(1,6)   # random dice roll, add it to current total
    print("Finished Rolling dice")
    print("Total rolled: " + str(diceResult))


#############################################
# End of function definitions, Start functional logic:
programActive = True # variable tells the code if it should loop again, or exit if the user entered 'q'
while programActive:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Please choose a game to play")
    print("Available games:")
    print(" 1 - Rock, Paper, Scissors")
    print(" 2 - Tic-Tac-Toe (WIP)")
    print(" 3 - Higher or Lower")
    print(" 4 - Dice Roll")
    gameChoice = input("Which game mode would you like to play? (number, or q to quit) ")
    if gameChoice == 'q':
        programActive = False # exits program
    elif gameChoice == '1':
        gameRPS()            # runs the rock paper scissors game function
        time.sleep(2) # waits for 2 seconds, helps user see end of game
    elif gameChoice == '2':
        gameTTT()            # runs the Tic Tac Toe game function
        time.sleep(2)
    elif gameChoice == '3':
        gameHOL()            # runs the Guess the Number game function
        time.sleep(2)
    elif gameChoice == '4':
        gameDICE()
        time.sleep(24)
    else:
        print("Invalid game choice, please try again")

print("Thanks for playing!")


