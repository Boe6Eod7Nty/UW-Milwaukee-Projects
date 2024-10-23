import random

#TIC TAC TOE
"REFERENCED FROM CDcodes's video: https://www.youtube.com/watch?v=Q6CCdCBVypg"

#used to clear board
import os

#displays slots on intiial board
spots = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}

playing = True
complete = False
turn = 0
prev_turn = -1

'''                     This break for some reason oops.
def getAImove():
    availableMoves = []
    for spot in spots:
        if not (spots[spot] == 'X' or spots[spot] == "O"):
            break
        else:
            availableMoves.append(spot)
    print(availableMoves)
    return random.choice(availableMoves)
'''

def draw_board(spots):

    #defines board spots using f-string
    board = (f"|{spots[7]}|{spots[8]}|{spots[9]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[1]}|{spots[2]}|{spots[3]}|")
    print(board)


def check_turn(turn):

    #checks turn with modulo operator;if remainder is 0, it's even and returns O, if remainder is 1, it's odd and returns X
    if turn % 2 == 0: return 'O'
    else: return 'X'


def check_for_win(spots):
    #Horitontal Cases
    if (spots[1] == spots[2] == spots[3]) \
        or (spots[4] == spots[5] == spots[6]) \
        or (spots[7] == spots[8] == spots[9]):
        return True
    #Vertical Cases
    elif (spots[1] == spots[4] == spots[7]) \
        or (spots[2] == spots[5] == spots[8]) \
        or (spots[3] == spots[6] == spots[9]):
        return True
    #Diagonal Cases
    elif (spots[1] == spots[5] == spots[9]) \
        or (spots[3] == spots[5] == spots[7]):
        return True


while playing:

    #Resets the screen when a move is made
    os.system('cls' if os.name == 'nt' else 'clear')

    draw_board(spots)
    if prev_turn == turn:
        print("\nInvalid entry, please enter another value")

    prev_turn = turn

    print("\nPlayer " + str((int(turn) % 2) + 1) +
          "'s turn: Pick your spot (or press 'Q' to quit)")

    # print("Computer recommends: " + str(getAImove())) disabled with getAImove() function

    #Gets player input
    choice = input()

    #quits the game
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
        #Check if spot has been taken
        if not spots[int(choice)] in {"X", "O"}:

            #int() fuction for players to enter valid input of 1-9 to place an X or O on the board
            turn += 1
            spots[int(choice)] = check_turn(turn)

    #check if game has ended
    if check_for_win(spots): playing, complete = False, True
    if turn > 8:
        playing = False
        #Resets the screen when a move is made
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(spots)

    #If there is a winner, say who won
    if complete:
        #Resets the screen when a move is made
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(spots)

        if check_turn(turn) == 'X': print("\nPlayer 1 Wins!")

        else: print("\nPlayer 2 Wins!")

    else:
        #Resets the screen when a move is made
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(spots)

        #Tie Game
        print("No Winner")

print("Thanks for playing!")
