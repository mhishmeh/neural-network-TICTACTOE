import random
import time


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
history = []


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


def saveBoardState(board, history):
    newBoard = [row[:] for row in board]  # Creates a deep copy of the board
    history.append(newBoard)  # Store this new snapshot in history




def isSpotTaken(board, row, column):
    if board[row][column] != ' ':
        return True
    return False

def getPlayer1Move():
    needInput = True
    
    while (needInput):
         userInput = int(input('PLayer One: Please place a move on the board! enter a numebr 1 thru 9: '))
         if userInput < 1 or userInput > 9:
            print('sorry, try again 1 through 9: ')
         else:
  
            positions = [
                    (0, 0), (0, 1), (0, 2),
                    (1, 0), (1, 1), (1, 2),
                    (2, 0), (2, 1), (2, 2)
            ]
            row, col = positions[userInput - 1]  # Get the correct row and column from the list 
            if isSpotTaken(board,row,col) == False:
                board[row][col] = player1Symbol
                saveBoardState(board, history)
                needInput = False
            else:
                print('sorry, spot is taken! Try again:')
    showBoard(board)

def getPlayer2Move():
    needInput = True
    
    while (needInput):
         userInput = int(input('PLayer Two: Please place a move on the board! enter a numebr 1 thru 9: '))
         if userInput < 1 or userInput > 9:
            print('sorry, try again 1 through 9: ')
         else:
  
            positions = [
                    (0, 0), (0, 1), (0, 2),
                    (1, 0), (1, 1), (1, 2),
                    (2, 0), (2, 1), (2, 2)
            ]
            row, col = positions[userInput - 1]  # Get the correct row and column from the list 
            if isSpotTaken(board,row,col) == False:
                board[row][col] = player2Symbol
                saveBoardState(board, history)
                needInput = False
            else:
                print('sorry, spot is taken! Try again:')
    showBoard(board)


def checkWinner():
    for item in board:
        pass

def playGame():
    while True:

        getPlayer1Move()
        getPlayer2Move()

playGame()
print(history)
