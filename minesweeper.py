"""
Kevin Lin
4/10/22
Minesweeper
"""
import random
import time
#actual field is 7x7 but list is 9x9 to remove special cases
key = [[0,0,0,0,0,0,0,0,0],#key field, contains all the mines and data
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0]]

board = [['x','x','x','x','x','x','x','x','x'],#9x9 to use same print method
        ['x','x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x','x'],
        ['x','x','x','x','x','x','x','x','x']]

mineNum=0
vis = []#which pieves have been visited, for revealing the 0's and preventing them from going into infinite recursion loop
moves = 0
flags = 0#how many flags are placed

def setUp():
    global mineNum
    while True:
        try:
            mines = ord(
                input("Welcome to minesweeper, would you like the default 10 mines or a custom amount?(d/c) ").lower())
            while mines<99 or mines>100:
                print("why")
                mines = ord(input(
                    "Welcome to minesweeper, would you like the default 10 mines or a custom amount?(d/c) ").lower())
            break
        except TypeError:
            print("why")

    if mines == 100:
        mineNum = 10
    elif mines == 99:
        while True:
            try:
                mineNum = int(input(
                    "How many mines do you want?(Must be more than 0 and at most 49[WARNING: BIGGER NUMBER MEANS LONGER START TIME]) "))
                while mineNum<=0 or mineNum>49:
                    print("why")
                    mineNum = int(input(
                        "How many mines do you want?(Must be more than 0 and at most 49[WARNING: BIGGER NUMBER MEANS LONGER START TIME]) "))
                break
            except ValueError:
                print("why")

def minePlace():#mine placer
    for x in range(mineNum):
        row = random.randrange(1,7)
        col = random.randrange(1,7)
        while key[row][col]==9:
            row = random.randrange(1, 7)
            col = random.randrange(1, 7)
        key[row][col] = 9

def mineFind():#mine finder
    for row in range(1,8):
        for col in range(1,8):
            if key[row][col]!=9:
                if key[row-1][col-1]==9:#top left -1,-1
                    key[row][col]+=1
                if key[row-1][col]==9:#top -1,0
                    key[row][col]+=1
                if key[row-1][col+1]==9:#top right -1,+1
                    key[row][col]+=1
                if key[row][col-1]==9:#left 0,-1
                    key[row][col]+=1
                if key[row][col+1]==9:#right 0,+1
                    key[row][col]+=1
                if key[row+1][col-1]==9:#bottom left +1,-1
                    key[row][col]+=1
                if key[row+1][col]==9:#bottom  +1,0
                    key[row][col]+=1
                if key[row+1][col+1]==9:#bottom right +1,+1
                    key[row][col]+=1

def fieldPrint(field):
    print("    a b c d e f g")
    print("    - - - - - - -")
    for x in range(1,8):
        for y in range(1,8):
            if(y==1):
                print(x,"|", end=" ")
            print(field[x][y], end=" ")
        print("|")
    print("    - - - - - - -")
    print()

def colChange(col):#returns number value of a letter
    return ord(col)-96

def getCoords():
    global moves
    moves +=1
    while True:
        try:
            row = int(input("Enter the row NUMBER(1-7): "))
            while (row > 7 or row < 1):
                print("why")
                row = int(input("Enter the row NUMBER(1-7): "))
            break
        except ValueError:
            print("why")


    while True:
        try:
            col = input("Enter the column LETTER(a-g): ").lower()
            while ord(col) < 97 or ord(col) > 103:
                print("why")
                col = input("Enter the column LETTER(a-g): ").lower()
            break
        except TypeError:
            print("why")

    coords = [row,colChange(col)]
    return coords

def reveal(row,col):
    global vis
    if key[row][col]==9:
        gameOver()
    elif [row,col] not in vis:
        vis.append([row,col])
        if row!=0 and row!=8 and col!=0 and col!=8:
            if key[row][col]==0:
                board[row][col] = key[row][col]
                reveal(row-1,col-1)
                reveal(row-1,col)
                reveal(row-1,col+1)
                reveal(row,col-1)
                reveal(row,col+1)
                reveal(row+1,col-1)
                reveal(row+1,col)
                reveal(row+1,col+1)
            if key[row][col]!=0:
                board[row][col]=key[row][col]

def gameOver():
    global gameOn
    global win
    gameOn = False
    win = False
    print("\nyou hit a mine")
    print("\nMine locations(9 is the mine)")
    fieldPrint(key)
    print("Your board")
    fieldPrint(board)

def flag(row,col):
    global flags
    while True:
        try:
            wantFlag = ord(input("Would you like to flag/unflag this tile?(y/n) ").lower())
            while wantFlag>122 or wantFlag<97:
                print("why")
                wantFlag = ord(input("Would you like to flag/unflag this tile?(y/n) ").lower())
            break
        except TypeError:
            print("why")

    if wantFlag==121:
        if ord(str(board[row][col])) >= ord('0') and ord(str(board[row][col])) < ord('9'):
            print("it's clear... why")
        elif board[row][col]=='*':
            unflag = ord(input("Already flagged, would you like to unflag?(y/n) ").lower())
            if unflag == 121:
                board[row][col] = 'x'
                flags-=1
            elif unflag == 110:
                pass
            else:
                print("why")
        else:
            board[row][col]='*'
            flags+=1
    elif wantFlag==110:
        reveal(row, col)
    else:
        print("why")
        flag(row,col)

def didWin():
    minesFound=0
    for x in range(1,8):
        for y in range(1,8):
            if board[x][y]=='*' and key[x][y]==9:
                minesFound+=1
                if minesFound==mineNum and flags==mineNum:
                    global gameOn
                    gameOn=False
                    print("\nGood Job, you won")
                    print("\nMine locations(9 is the mine)")
                    fieldPrint(key)
                    print("Your board")
                    fieldPrint(board)

#gamecode
setUp()
minePlace()
mineFind()

win = True
gameOn = True
start = time.time()#time start
while gameOn:
    coords = getCoords()
    flag(coords[0],coords[1])
    didWin()
    if not gameOn:
        end = time.time()#time end
        break
    fieldPrint(board)

if win==True:
    result = "complete"
elif win==False:
    result = "lose on"
if mineNum==1:
    if moves==1:
        print("It took you", moves, "move and", format(end - start, ".3f"), "seconds to", result, "a 7x7 board with",
              mineNum, "mine")
    else:
        print("It took you", moves, "moves and", format(end - start, ".3f"), "seconds to", result, "a 7x7 board with",
              mineNum, "mine")
else:
    if moves==1:
        print("It took you", moves, "move and", format(end - start, ".3f"), "seconds to", result, "a 7x7 board with",
          mineNum, "mines")
    else:
        print("It took you", moves, "moves and", format(end - start, ".3f"), "seconds to", result, "a 7x7 board with",
              mineNum, "mines")