import random
import time


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def showBoard(board):
    for row in board:
        print(" | ".join(row))
        print('-' * 9)


showBoard(board)
time.sleep(.5)
def definePlayers():
    global player1Symbol, player2Symbol
    symbol = random.randint(0,1)
    if symbol == 0:
        player1Symbol ='O'
        player2Symbol = 'X'
    else:
        player1Symbol = 'X'
        player2Symbol = 'O'

definePlayers()

def getPlayer1Move():
    needInput = True
    userInput = int(input('Please place a move on the board! enter a numebr 1 thru 9: '))
    while (needInput):
         if userInput < 1 or userInput > 9:
            print('sorry, try again 1 through 9: ')
         else:
            needInput = False
            break
    else:
        if userInput == 1:
            board[0][0] = player1Symbol
        if userInput == 2:
            board[0][1] = player1Symbol
        if userInput == 3:
            board[0][2] = player1Symbol
        if userInput == 4:
            board[1][0] = player1Symbol
        if userInput == 5:
            board[1][1] = player1Symbol
        if userInput == 6:
            board[1][2] = player1Symbol
        if userInput == 7:
            board[2][0] = player1Symbol
        if userInput == 8:
            board[2][1] = player1Symbol
        if userInput == 9:
            board[2][2] = player1Symbol
    showBoard(board)

getPlayer1Move()
