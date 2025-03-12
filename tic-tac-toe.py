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
         if type(userInput) != int:
            print('dumbass, obviously you need to enter a number please. TRY AGAIN YOU can do it. you can be somebody in this')
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

def getAIMove():
    aiChoices = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                aiChoices.append((row,col))

    row, col = random.choice(aiChoices)
    board[row][col] = player2Symbol
    showBoard(board)


def checkWinner():
    for row in board: # check rows
        if row[0] == row[1] and  row[0] == row[2] and row[0] != ' ':
            print('Congrats! '+ row[0] + ' Player has won!')
            return True

    for col in range(3): # columns
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != ' ':
            print('fuck you fucking won bro.')
            return True

    
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != ' ':
        print('haha nice bro! ' + board[0][0] + ' has won!' )
        return True
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != ' ':
        print("ahhh man shit! ya GGOT ME!" + board[2][0] + ' has won!')
        return True
        

def playGame():
    count = 0
    gameState = True
    while gameState:
        if count == 9:
            print('ahhhh! scratch. play again')
            break
        getPlayer1Move()
        count += 1
    
        if checkWinner():
            break

        getAIMove()
        count += 1
      
        if checkWinner():
            break
        

playGame()
print(history)
