# A 2 player connect four game with a simple text display

# ***********************Game Functions*************************************

def zeroout ():
    # making a zeroed out move list --first time only
    count = 0
    moves = []
    while count < 42:
        moves.append(0)
        count = count + 1
    return moves

def colzero():
    # making a zeroed out columlist
    height = []
    count = 0
    while count < 7:
        height.append(int(0))
        count = count + 1
    return height

def warningzero():
    # making a zeroed out overflow warning
    spotWarning = False
    count = 0
    warning = []
    while count < 7:
        warning.append(spotWarning)
        count +=1
    return warning

def moveinput():
    # input the move
    moveInput = raw_input("Enter Move (columns 1-7 left to right): ")
    switch = "off"
    # check for a valid move
    while switch == "off":
        try:
            n1 = int(moveInput)
        except ValueError:
            moveInput = raw_input("Not a number.  Please enter a number 1-7:")
        else:
            if int(moveInput) < 8 and int(moveInput) > 0 and warning[int(moveInput) - 1] == False:
                switch = "on" 
            else:
                moveInput = raw_input("Input a valid move (1-7):  ")
    moveInput = int(moveInput) 
    return moveInput

def movelocator(move, moveList, colHeight):
    # finds move in moveList
    checkColumn = move - 1
    heightTimes = colHeight[checkColumn] 
    spot = heightTimes * 7 + checkColumn
    return spot

def wincheck(moveList, playerTurn, move, row):
    winner = "off"
    w = 0
    high = w
    # check horizontally   
    col = 0
    start = (row) * 7
    while col < 7:
        if moveList[start + col] == playerTurn:
            w += 1
            if w > high:
                high = w
        else:
            w = 0
        if w == 4:
            winner = "on"
        col += 1
    # check vertically
    w = 0
    start = move - 1
    count = 0
    while count < 6:
        if moveList[start] == playerTurn:
            w += 1
            if w > high:
                high = w
        else:
            w = 0
        if w == 4:
            winner = "on"
        count += 1
        start = start + 7
    # check diag /
    w = 0
    cornerFound = False
    start = (move - 1) + (row * 7)
    # find bottom left spot to check
    while start >= 0:
        start = start - 8
    start = start + 8
    # check through / diagonal
    finished = False
    remainder = start % 7
    while not finished:
        if remainder < 7:
            try: 
                if moveList[start] == playerTurn:
                    w += 1   
                    if w > high:
                        high = w      
                else:
                    w = 0
                if w == 4:
                    winner = "on"
            except IndexError:
                finished = True
            start = start + 8
            remainder += 1
        else:
            finished = True

    # check diag \
    # find bottom right corner
    w = 0
    start = (move - 1) + (row * 7)
    remainder = start % 7
    checky = False
    while remainder < 7 and row > 0:
        start = start -6
        remainder += 1
        row += 1
        checky = True
    if checky:
        start = start + 6
    # check through \ diagonal
    finished = False
    remainder = start % 7
    while not finished:
        if remainder >= 0:
            try: 
                if moveList[start] == playerTurn:
                    w += 1   
                    if w > high:
                        high = w      
                else:
                    w = 0
                if w == 4:
                    winner = "on"
            except IndexError:
                finished = True
            start = start + 6
            remainder = remainder - 1
        else:
            finished = True

    print high, "in a row."
    return winner

# ***************************Gameplay below*****************************************



# if game hasn't started, zero out lists
try:
    gameStart
except NameError:
    moveList = zeroout()
    colHeight = colzero()
    warning = warningzero()
    gameStart = "on"
    turn = 1
    playerTurn = turn % 2 + 1
    winner = "off"

tie = False

print "===========================TURN %s START===============================" % turn 
print "Player %s turn" % str(playerTurn - 1)

while winner == "off":

    # player inputs the move
    move = moveinput()

    # find move in moveList
    spot = movelocator(move, moveList, colHeight)

    # add move to moveList
    moveList[spot] = playerTurn

    # wincheck
    winner = wincheck(moveList, playerTurn, move, colHeight[move - 1])

    # change colHeight
    colHeight[move - 1] +=1
 
    # overflowcheck
    if colHeight[move - 1] == 6:
        warning[move - 1] = True

    # check for a tie
    if all(i == True for i in warning):
        tie = True
        winner = "on"

    #quick display
    dis = 35
    while dis < 42:
        if moveList[dis] == 0:
            checker = "_"
        if moveList[dis] == 1:
            checker = "O"
        if moveList[dis] == 2:
            checker = "X"
        print checker, "|",
        dis += 1
    dis = 28
    print " "
    while dis < 35:
        if moveList[dis] == 0:
            checker = "_"
        if moveList[dis] == 1:
            checker = "O"
        if moveList[dis] == 2:
            checker = "X"
        print checker, "|",
        dis += 1
    dis = 21
    print " "
    while dis < 28:
        if moveList[dis] == 0:
            checker = "_"
        if moveList[dis] == 1:
            checker = "O"
        if moveList[dis] == 2:
            checker = "X"
        print checker, "|",
        dis += 1
    dis = 14
    print " "
    while dis < 21:
        if moveList[dis] == 0:
            checker = "_"
        if moveList[dis] == 1:
            checker = "O"
        if moveList[dis] == 2:
            checker = "X"
        print checker, "|",
        dis += 1
    dis = 7
    print " "
    while dis < 14:
        if moveList[dis] == 0:
            checker = "_"
        if moveList[dis] == 1:
            checker = "O"
        if moveList[dis] == 2:
            checker = "X"
        print checker, "|",
        dis += 1
    dis = 0
    print " "
    while dis < 7:
        if moveList[dis] == 0:
            checker = "_"
        if moveList[dis] == 1:
            checker = "O"
        if moveList[dis] == 2:
            checker = "X"
        print checker, "|",
        dis += 1
    print " "




    if winner == "off":
        print "===========================TURN %s START===============================" % str(turn + 1)
        print "Player %s turn" %playerTurn

    # change turn
    turn = turn + 1
    playerTurn = turn % 2 + 1


if tie == False:
    print "****************************Player %s Wins**************************" % playerTurn
else:
    print "********************************Tie*********************************"

