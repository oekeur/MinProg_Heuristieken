# An implementation of a game of rushhour
# Ultimate goal is to get a algorithm (BFS probably) get to solve at least 6 given puzzles
#
# Names: Kyra Kieskamp & Oscar Keur
# Stud.no.: 10099727 & 11122102
#

import time      # to use wait when visualizing
import pygame    # to use visuals
import csv       # to use csv.reader
import random    # to make automated random moves
import copy      # for using deepcopy

nummovestot = [5000]

    # initialize some vars
def InitializeVariables():
    global moves1, moves2, moves, archive, hashval, nummoves, colours, movesmade, oldx, oldy
    moves1 = {}       # dictionary: key=id, value=move, holds all moves up or left
    moves2 = {}       # dictionary: key=id, value=move, holds all moves down or right
    move = []         # list with: car to move, to which y, x
    archive =  set()  # set: value=hashedmatrix
    cars = []         # list of list with ID, orientation, length, y and x
    Rmatrix = [[]]    # List of list representing a matrix
    boardsize = 0     # integer to initialy build up an empty board
    hashval = ""      # not really hashed, a string that depicts the position of each car
    nummoves = 0      # number of moves done
    oldy = 0          # for storing the last move, if the car has to reverse
    oldx = 0          # for storing the last move, if the car has to reverse
    movesmade = []    # List of movesmade, for reproducing


######################################################################################
    # Helperfunctions, board related
######################################################################################
def InitBoard(boardname):
    InitializeVariables()
    global Rmatrix, boardsize
    cars = []
    Rmatrix = [[]]
    boardsize = 0
    boardname = "boards/board" + str(boardname) + ".csv"
    # open the board
    csvfile = open(boardname)
    boardfile = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    next(boardfile)
    boardsize = int(next(boardfile)[0])
    # add the cars from file to a list of cars
    for row in boardfile:
        cars.append(row)
    # convert to int what an int should be
    i = 0
    for car in cars:
        cars[i][2] = int(cars[i][2])
        cars[i][3] = int(cars[i][3]) - 1
        cars[i][4] = int(cars[i][4]) - 1
        i += 1
    # define the board itself
    Rmatrix = UpdateWholeBoard(cars)
    return (cars, Rmatrix, boardsize)

def UpdateWholeBoard(cars):
    Rmatrix = [['0' for x in range(boardsize)] for y in range(boardsize)]
    i = 0
    # for each car
    for car in cars:
        # location of front is occupied at board
        Rmatrix[cars[i][3]][cars[i][4]] = cars[i][0]
        # if orientation is horizontal update the tile to the right from last tile
        if cars[i][1] == 'h':
            Rmatrix[cars[i][3]][cars[i][4]+1] = cars[i][0]
            # if the length of the car is 3, also occupy the next tile
            if cars[i][2] == 3:
                Rmatrix[cars[i][3]][cars[i][4]+2] = cars[i][0]
        # same for vertical orientation
        else:
             Rmatrix[cars[i][3]+1][cars[i][4]] = cars[i][0]
             if cars[i][2] == 3:
                Rmatrix[cars[i][3]+2][cars[i][4]] = cars[i][0]
        i += 1
    return Rmatrix

######################################################################################
    # Helperfunctions, determining moves related
######################################################################################

def AllPossibleMoves(cars, Rmatrix):
    i = 0
    moves1.clear()
    moves2.clear()
    for car in cars:
        if cars[i][1] == 'h':
            x = cars[i][4] - 1
            y = cars[i][3]
            if isValidMove(x,y,Rmatrix): # go left
                moves1[i] = [y,x]

            x = cars[i][4] + cars[i][2]
            y = cars[i][3]
            if isValidMove(x,y,Rmatrix): # go right
                x = cars[i][4] + 1
                moves2[i] = [y,x]
        # if orientation is vertical        
        else: 
            y = cars[i][3] - 1
            x = cars[i][4]
            if isValidMove(x,y,Rmatrix): # go up
                moves1[i] = [y,x]

            y = cars[i][3] + cars[i][2]
            x = cars[i][4]
            if isValidMove(x,y,Rmatrix): # go down
                y = cars[i][3] + 1
                moves2[i] = [y,x]
        i += 1
    return (moves1, moves2)

def OnePossibleMove(i):
    if cars[i][1] == 'h':
        x = cars[i][4] - 1
        y = cars[i][3]
        if isValidMove(x,y, Rmatrix): # go left
            moves1[i] = [y,x]

        x = cars[i][4] + cars[i][2]
        y = cars[i][3]
        if isValidMove(x,y, Rmatrix): # go right
            x = cars[i][4] + 1
            moves2[i] = [y,x]

    else: # if orientation is vertical
        y = cars[i][3] - 1
        x = cars[i][4]
        if isValidMove(x,y, Rmatrix): # go up
            moves1[i] = [y,x]

        y = cars[i][3] + cars[i][2]
        x = cars[i][4]
        if isValidMove(x,y, Rmatrix): # go down
            y = cars[i][3] + 1
            moves2[i] = [y,x]
    return (moves1, moves2)

######################################################################################
    # Helperfunctions, choosing a move
######################################################################################

def ChooseRandomMove(moves1, moves2):
    if bool(moves1) and bool(moves2): # returns false on an empty dict
        moveid = random.choice(random.choice([moves1, moves2]).keys())
        x = random.randint(0,1)
        if x == 0:
            if moves1.get(moveid) == None:
                movexy = moves2.get(moveid)
            else:
                movexy = moves1.get(moveid)
        else:
            if moves2.get(moveid) == None:
                movexy = moves1.get(moveid)
            else:
                movexy = moves2.get(moveid)

    elif bool(moves1) and not bool(moves2): # if moves 2 is empty
        moveid = random.choice(random.choice([moves1]).keys())
        movexy = moves1.get(moveid)

    elif not bool(moves1) and bool(moves2): # if moves 1 is empty
        moveid = random.choice(random.choice([moves2]).keys())
        movexy = moves2.get(moveid)

    move = [moveid , movexy]

    return move

def PrefRandomMove(moves1, moves2):
    if bool(moves1) and bool(moves2): # returns false on an empty dict
        moveid = random.choice(random.choice([moves1, moves2]).keys())
        x = random.randint(0,2)
        if x >= 1:
            if moves1.get(moveid) == None:
                movexy = moves2.get(moveid)
            else:
                movexy = moves1.get(moveid)
        else:
            if moves2.get(moveid) == None:
                movexy = moves1.get(moveid)
            else:
                movexy = moves2.get(moveid)

    elif bool(moves1) and not bool(moves2): # if moves 2 is empty
        moveid = random.choice(random.choice([moves1]).keys())
        movexy = moves1.get(moveid)

    elif not bool(moves1) and bool(moves2): # if moves 1 is empty
        moveid = random.choice(random.choice([moves2]).keys())
        movexy = moves2.get(moveid)

    move = [moveid , movexy]

    return move

######################################################################################
    # Helperfunctions, moving cars
######################################################################################
def MoveCar(move, cars):
    i = move[0] # list with move to make
    y = move[1][0]
    x = move[1][1]
    oldy = cars[i][3]
    oldx = cars[i][4]
    # if the car moves up or left, reset the old tail
    if y < cars[i][3] or x < cars[i][4]:
        if cars[i][1] == 'h':
            Rmatrix[cars[i][3]][x + cars[i][2]] = "0"
        else:
            Rmatrix[y + cars[i][2]][cars[i][4]] = "0"
    # if it moves right or down, reset the old head
    else:
        Rmatrix[cars[i][3]][cars[i][4]] = '0'

    Rmatrix[y][x] = cars[i][0]
    # if orientation is horizontal update the tile to the right from last tile
    if cars[i][1] == 'h':
        Rmatrix[y][x+1] = cars[i][0]
        # if the length of the car is 3, also occupy the next tile
        if cars[i][2] == 3:
            Rmatrix[y][x+2] = cars[i][0]
    # same for vertical orientation
    else:
         Rmatrix[y+1][x] = cars[i][0]
         if cars[i][2] == 3:
            Rmatrix[y+2][x] = cars[i][0]
    # Edit list of cars
    cars[i][3] = y
    cars[i][4] = x
    return (Rmatrix, oldy, oldx, cars)

def ReverseMoveCar(oldy, oldx, cars, move):
    move[1][0] = oldy
    move[1][1] = oldx
    MoveCar(move, cars)
    return (Rmatrix, cars)

######################################################################################
        # Helperfunctions, evaluation
######################################################################################
def isValidMove(x, y, Rmatrix):
  """"
  Return True if the move is valid (on board and free)
  """
  if 0 <= x < boardsize and 0 <= y < boardsize and Rmatrix[y][x] == '0':
      return True
  else:
      return False

def EvaluateState(Rmatrix, move, cars):
    hashval = DetermineBoardState(Rmatrix, move, cars)
    if hashval not in archive:
        archive.add(hashval)
        return True
    else:
        return False

def DetermineBoardState(Rmatrix, move, cars):
    # make a move on the matrix in local scope
    Rmatrix, oldy, oldx, cars = MoveCar(move, cars)
    hashval = ""
    i = 0
    for column in Rmatrix:
        j = 0
        for row in column:
            hashval += Rmatrix[j][i]
            j += 1
        i += 1
    return hashval


######################################################################################
    # Gamesequences
######################################################################################

def GameOn_Random(k, board):
    nummoves = 0
    cars, Rmatrix, boardsize = InitBoard(board)
    while cars[0][4] != (boardsize - 2) :
        moves1, moves2 = AllPossibleMoves(cars, Rmatrix)
        move = ChooseRandomMove(moves1, moves2)
        Rmatrix, oldy, oldx, cars = MoveCar(move, cars)
        movesmade.append(move)
        # time.sleep(.100)
        # VisualizeCars(cars)
        nummoves += 1
        if nummoves > min(nummovestot):
            break
    if nummoves < min(nummovestot):
        nummovestot.append(nummoves)
        print 'EXIT!', k , nummoves, nummovestot

def GameOn_Random_Num(board, n):
    global k
    k = 0
    while k < n:
        GameOn_Random(k, board)
        k += 1
        if k % 1000 == 0:
            print "I'm still alive"
    print "Board", board, "Minmoves:", min(nummovestot), "Solutions found:", len(nummovestot) -1, "Iterations: ", k        

def GameOn_Algo(boardname):
    cars, Rmatrix, boardsize = InitBoard(boardname)
    i = 0
    carid = [0]
    while cars[0][4] != (boardsize - 2):
        moves1, moves2 = OnePossibleMove(carid[-1])
        # if the targetcar is currently selected, move it
        if carid[-1] == 0:
            if bool(moves1) or bool(moves2):
                move = PrefRandomMove(moves1, moves2)
                Rmatrix, cars = MoveCar(move, cars)
            carid.append()

        # else, determined if the selected car has space to move
        else:
            if bool(moves1) or bool(moves2):
                move = PrefRandomMove(moves1, moves2)
                Rmatrix, cars = MoveCar(move, cars)
            carid.append()


def BreadthFirst(boardname):
    global nummoves, iteration # to make sure rushhour.py can access the variable
    from collections import deque
    cars, Rmatrix, boardsize = InitBoard(boardname)
    cars[0].append(0)

    # create a deque 
    Breadth_list = deque()  
    Breadth_list.append(cars)
    List_done = deque()
    List_done.append(0)
    nummoves, olddepth, iteration = (0, 0, 0)

    # time.sleep(0.100)
    # VisualizeCars(cars)

    while (0 < Breadth_list.count):
        # possible moves
        cars = copy.deepcopy(Breadth_list[0])
        Rmatrix = UpdateWholeBoard(cars)
        moves1, moves2 = AllPossibleMoves(cars, Rmatrix)

        # moves in move2
        for car in moves1:
            Breadth_cars = copy.deepcopy(cars)
            Breadth_cars[car][3] = moves1[car][0]
            Breadth_cars[car][4] = moves1[car][1]

            # solution found --> exit
            if Breadth_cars[0][4] == (boardsize -2):
                print 'EXIT! in', Breadth_cars[0][5] + 1, 'moves, we had to try', iteration, 'boards'
                nummoves = Breadth_cars[0][5]  + 1   
                return

            # saving the list of cars if never been in this state
            elif (Breadth_list.count(Breadth_cars) == 0 and Breadth_cars not in List_done):
                Breadth_cars[0][5] += 1
                Breadth_list.append(Breadth_cars)
                # time.sleep(0.100)
                # VisualizeCars(Breadth_cars)

        # moves in moves2
        for car in moves2:
            Breadth_cars[car][3] = moves2[car][0]
            Breadth_cars[car][4] = moves2[car][1]

            if Breadth_cars[0][4] == (boardsize -2):
                print 'EXIT! in', Breadth_cars[0][5] + 1, 'moves, we had to try', iteration, 'boards'
                nummoves = Breadth_cars[0][5] + 1
                return

            elif Breadth_list.count(Breadth_cars) == 0 and Breadth_cars not in List_done:
                Breadth_cars[0][5] += 1
                Breadth_list.append(Breadth_cars)
                # time.sleep(0.100)
                # VisualizeCars(Breadth_cars)
        iteration += 1
        # updat moves, remove cars from Breadth_list and add to List_done
        done = Breadth_list.popleft()
        List_done.append(done)
        # print nummoves, "number of boards"
        moves1.clear()
        moves2.clear()




def DepthFirst(board, maxdepth):
    global iteration
    depth, oldy, oldx, iteration = (0, 0, 0, 0)
    move = []
    cars, Rmatrix, boardsize = InitBoard(board)
    # time.sleep(0.150)
    # VisualizeCars(cars)
    while cars[0][4] != (boardsize - 2) :
        Rmatrix = UpdateWholeBoard(cars)
        depth, oldy, oldx, move, Rmatrix, cars = DepthSearch(depth, maxdepth, cars, Rmatrix, oldy, oldx, move)
        iteration += 1

    print 'EXIT! in', len(movesmade), 'moves, we had to try', iteration, 'boards'

def DepthSearch(depth, maxdepth, cars, Rmatrix, oldy, oldx, move):
    global movesmade
    if depth >= maxdepth:
        movesmade.pop()
        Rmatrix, cars = ReverseMoveCar(oldy, oldx, cars, move)
        depth -= 1

    moves1, moves2 = AllPossibleMoves(cars, Rmatrix)
    move = ChooseRandomMove(moves1, moves2)

    if EvaluateState(Rmatrix, move, cars): #returns false when board has already been done
        movesmade.append(move)
        Rmatrix, oldy, oldx, cars = MoveCar(move, cars)
        # time.sleep(0.100)
        # VisualizeCars(cars)
        depth += 1
    elif depth > 0:
        # movesmade.pop()
        depth -= 1
    return (depth, oldy, oldx, move, Rmatrix, cars)

######################################################################################
    # Visualisation
######################################################################################

def VisualizeCars(cars):
    background_colour = (255, 255, 255)
    (width, height) = (700, 600)
    padding = 20
    colours = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 150, 0), (150, 0, 0), (0, 0, 150), (150, 150, 150), (95, 10, 10), (10, 95, 10), (10, 10, 95)]

    # visualization screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Rushhour, board 1")
    screen.fill(background_colour)

    # board framework
    pygame.draw.rect(screen, (0, 0, 255), (padding, padding, (width - (padding + padding)), (height - (padding + padding))), 2)

    # board lines
    blocklength = (width- (padding + padding))/boardsize
    blockheight = (height-(padding + padding))/boardsize
    for i in range (1, boardsize):
        xposition = blocklength * i
        yposition = blockheight * i
        pygame.draw.line(screen, (0, 0, 255), (padding + xposition, padding), (padding + xposition, height - padding))
        pygame.draw.line(screen, (0, 0, 255), (padding, padding + yposition), (width - padding, padding + yposition))

    # Clear board except for the board lines - override
    # draw cars
    # text = nummoves
    # pygame.font.init()
    # pygame.font.Font.render(text, 0, (0, 0, 0), background=None)

    i = 0
    # for each car
    for car in cars:
        # if orientation is horizontal update the tile to the right from last tile
        if cars[i][1] == 'h':
            if cars[i][2] == 2:
                pygame.draw.rect(screen, colours[i%10], (padding + (blocklength * cars[i][4]), padding + (blockheight * cars[i][3]), blocklength * 2, blockheight), 0)
                pygame.draw.rect(screen, (0, 0, 0), (padding + (blocklength * (cars[i][4] + 0.3)), padding + (blockheight * cars[i][3]), blocklength * 1, blockheight), 2)
                # front car
                pygame.draw.line(screen, (0, 0, 0), (padding + (blocklength * (cars[i][4] + 1.35)), padding + (blockheight * cars[i][3])), (padding + (blocklength * (cars[i][4] + 1.35)), \
                padding + (blockheight * (cars[i][3] + 1))))
                pygame.draw.line(screen, (0, 0, 0), (padding + (blocklength * (cars[i][4] + 1.35)), padding + (blockheight * cars[i][3])), (padding + (blocklength * (cars[i][4] + 2)), \
                padding + (blockheight * (cars[i][3] + 0.15))))
                pygame.draw.line(screen, (0, 0, 0), (padding + (blocklength * (cars[i][4] + 1.35)), padding + (blockheight * (cars[i][3] + 1))), (padding + (blocklength * (cars[i][4] + 2)), \
                padding + (blockheight * (cars[i][3] + 0.85))))
                # insert: nummoves variable in a block

                # AAfilledRoundedRect(screen, rect, color, radius = 0.4)
                # insert car lines
            else:
                pygame.draw.rect(screen, colours[i%10], (padding + (blocklength * cars[i][4]), padding + (blockheight * cars[i][3]), blocklength * 3, blockheight), 0)
                pygame.draw.rect(screen, (0, 0, 0), (padding + (blocklength * (cars[i][4] + 0.1)), padding + (blockheight * cars[i][3]), blocklength * 1.95, blockheight), 2)
                pygame.draw.rect(screen, (0, 0, 0), (padding + (blocklength * (cars[i][4] + 2.1)), padding + (blockheight * cars[i][3]), blocklength * 0.85, blockheight), 2)
        else:
            if cars[i][2] == 2:
                pygame.draw.rect(screen, colours[i%10], (padding + (blocklength * cars[i][4]), padding + (blockheight * cars[i][3]), blocklength, blockheight * 2), 0)
                pygame.draw.rect(screen, (0, 0, 0), (padding + (blocklength * cars[i][4]), padding + (blockheight * (cars[i][3] + 0.3)), blocklength, (blockheight * 1)), 2)
                # front car
                pygame.draw.line(screen, (0, 0, 0), (padding + (blocklength * cars[i][4]), padding + (blockheight * (cars[i][3] + 1.35))), (padding + (blocklength * (cars[i][4] + 1)), \
                padding + (blockheight * (cars[i][3] + 1.35))))
                pygame.draw.line(screen, (0, 0, 0), (padding + (blocklength * cars[i][4]), padding + (blockheight * (cars[i][3] + 1.35))), (padding + (blocklength * (cars[i][4] + 0.15)), \
                padding + (blockheight * (cars[i][3] + 2))))
                pygame.draw.line(screen, (0, 0, 0), (padding + (blocklength * (cars[i][4] + 1)), padding + (blockheight * (cars[i][3] + 1.35))), (padding + (blocklength * (cars[i][4] + 0.85)), \
                padding + (blockheight * (cars[i][3] + 2))))
            else:
                pygame.draw.rect(screen, colours[i%10], (padding + (blocklength * cars[i][4]), padding + (blockheight * cars[i][3]), blocklength, blockheight * 3), 0)
                pygame.draw.rect(screen, (0, 0, 0), (padding + (blocklength * cars[i][4]), padding + (blockheight * (cars[i][3] + 0.1)), blocklength, (blockheight * 1.95)), 2)
                pygame.draw.rect(screen, (0, 0, 0), (padding + (blocklength * cars[i][4]), padding + (blockheight * (cars[i][3] + 2.1)), blocklength, blockheight * 0.85), 2)
        i += 1

    pygame.display.flip()

    # uncomment this section if you want to view a single board
    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    # uncomment this section if you want to view a single board

######################################################################################
        # Helperfunctions, debugprint
######################################################################################
def debugprint():
    PrintBoard(Rmatrix)
    PrintCars(cars)
    PrintMoves(moves1, moves2)
    print "Move: ", move

def PrintBoard(Rmatrix):
    i = 0
    print "Boardmatrix:", "Move:", nummoves
    for row in Rmatrix:
        print (Rmatrix[i])
        i += 1

    print

def PrintCars(cars):
    i = 0
    print "List of cars:"
    for entry in cars:
        print i, ":", cars[i]
        i += 1
    print

def PrintMoves(moves1, moves2):
    print "Up/Left moves:", moves1, "      Down/Right moves:", moves2
