import random

# Jason Lines 
print("Welcome to gaming")

def gameRPS(): # RPS game function
    print("You are playing Rock Paper Scissors")
    ## get user input on their hand throw
    handform = input("Rock Paper or Scissors?").lower()

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
    player1move = input("It's your turn to choose a spot: ")
    
    spots = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
    
    board =  "\n"+spots[1]+"|"+spots[2]+"|"+spots[3]\
            +"\n"+spots[4]+"|"+spots[5]+"|"+spots[6]\
            +"\n"+spots[7]+"|"+spots[8]+"|"+spots[9]
    
    print(board)

programActive = True
while programActive:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Please choose a game to play")
    print("Available games:")
    print(" 1 - Rock, Paper, Scissors")
    print(" 2 - Tic-Tac-Toe")
    gameChoice = input("Which game mode would you like to play? (number, or q to quit) ")
    if gameChoice == 'q':
        programActive = False # exits program
    elif gameChoice == '1':
        gameRPS()            # runs the rock paper scissors game function
    elif gameChoice == '2':
        gameTTT()            # runs the Tic Tac Toe game function
    else:
        print("Invalid game choice, please try again")

print("Thanks for playing!")



def gameTTT():
    print("You are playing Tic-Tac-Toe")
    board = "\n1|2|3\n4|5|6\n7|8|9"
    print(board)
    player1move = input("It's your turn to choose a spot: ")

    spots = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

    board =  "\n"+spots[1]+"|"+spots[2]+"|"+spots[3]\
            +"\n"+spots[4]+"|"+spots[5]+"|"+spots[6]\
            +"\n"+spots[7]+"|"+spots[8]+"|"+spots[9]

    print(board)