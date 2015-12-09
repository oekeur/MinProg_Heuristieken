# An implementation of a game of rushhour
# Ultimate goal is to get a algorithm (BFS probably) get to solve at least 6 given puzzles
#
# Names: Kyra Kieskamp & Oscar Keur
# Stud.no.: 10099727 & 11122102
#
# Version: 0.1
# Changes: Skeleton to import a board an display it

import time # to calculate time needed
import pygame # to use visuals
# import sys # to use argv
import csv # to use csv.reader
import random # to make automated random moves
import visualize
import collections

nummovestot = [5000]

    # initialize some vars
def InitializeVariables():
    global moves1, moves2, moves, archive, cars, Rmatrix, boardsize, hashval, nummoves, colours, chosencar, nummovestot
    moves1 = {}       # dictionary: key=id, value=move, holds all moves up or left
    moves2 = {}       # dictionary: key=id, value=move, holds all moves down or right
    move = []         # list with: car to move, to which y, x
    archive =  set()  # set: value=hashedmatrix
    cars = []         # list of list with ID, orientation, length, y and x
    Rmatrix = [[]]    # List of list representing a matrix
    boardsize = 0     # integer to initialy build up an empty board
    hashval = ""      # not really hashed, a string that depicts the position of each car
    nummoves = 0      # number of moves done
    colours = []      # list of colours
    movesmade = []
    k = 0


    # Helperfunctions, board related
######################################################################################
def InitBoard():
    InitializeVariables()
    global cars, Rmatrix, boardsize
    # open the board
    csvfile = open('boards/board7.csv')
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
    UpdateWholeBoard()

def PrintBoard():
    i = 0
    print "Boardmatrix:", "Move:", nummoves
    for row in Rmatrix:
        print (Rmatrix[i])
        i += 1

    print

def PrintCars():
    i = 0
    print "List of cars:"
    for entry in cars:
        print i, ":", cars[i]
        i += 1
    print

def PrintMoves():
    print "Up/Left moves:", moves1, "      Down/Right moves:", moves2

def UpdateWholeBoard():
    global Rmatrix, cars
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

    # Helperfunctions, determining moves related
######################################################################################

def isValidMove(x, y):
  """"
  Return True if the move is valid (on board and free)
  """
  if 0 <= x < boardsize and 0 <= y < boardsize and Rmatrix[y][x] == '0':
      return True
  else:
      return False

def AllPossibleMoves():
    global moves1, moves2
    i = 0
    moves1.clear()
    moves2.clear()
    for car in cars:
        if cars[i][1] == 'h':
            x = cars[i][4] - 1
            y = cars[i][3]
            if isValidMove(x,y): # go left
                moves1[i] = [y,x]

            x = cars[i][4] + cars[i][2]
            y = cars[i][3]
            if isValidMove(x,y): # go right
                x = cars[i][4] + 1
                moves2[i] = [y,x]
        else: # if orientation is vertical
            y = cars[i][3] - 1
            x = cars[i][4]
            if isValidMove(x,y): # go up
                moves1[i] = [y,x]

            y = cars[i][3] + cars[i][2]
            x = cars[i][4]
            if isValidMove(x,y): # go down
                y = cars[i][3] + 1
                moves2[i] = [y,x]
        i += 1

def OnePossibleMove(i):
    global moves1, moves2
    if cars[i][1] == 'h':
        x = cars[i][4] - 1
        y = cars[i][3]
        if isValidMove(x,y): # go left
            moves1[i] = [y,x]

        x = cars[i][4] + cars[i][2]
        y = cars[i][3]
        if isValidMove(x,y): # go right
            x = cars[i][4] + 1
            moves2[i] = [y,x]

    else: # if orientation is vertical
        y = cars[i][3] - 1
        x = cars[i][4]
        if isValidMove(x,y): # go up
            moves1[i] = [y,x]

        y = cars[i][3] + cars[i][2]
        x = cars[i][4]
        if isValidMove(x,y): # go down
            y = cars[i][3] + 1
            moves2[i] = [y,x]

def ChooseRandomMove():
    global move
    if bool(moves1) and bool(moves2): # returns false on an empty dict
        moveid = random.choice(random.choice([moves1, moves2]).keys())
        x = random.randint(1,2)
        if x == 1:
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

    else: # no moves possible
        PrintBoard()
        PrintCars()
        raise Exception ('No moves possible!')

    move = [moveid , movexy]
    # PrintMoves()
    # print move



    # Helperfunctions, move related
######################################################################################
def MoveCar():
    global Rmatrix
    i = move[0] # list with move to make
    y = move[1][0]
    x = move[1][1]
    # print "We will move", cars[i][0], "to", y, x
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

        # Helperfunctions, evaluation
######################################################################################

def EvaluateState():
    DetermineBoardState()
    if hashval not in archive:
        archive.add(hashval)
        return True
    else:
        return False

def DetermineBoardState():
    global hashval
    # make a move on the matrix in local scope
    MoveCar()
    hashval = ""
    i = 0
    for column in Rmatrix:
        j = 0
        for row in column:
            hashval += Rmatrix[j][i]
            j += 1
        i += 1
    hashval += str(move)

def ChooseCar():

    chosencar.append(i)


    # Gamesequences
######################################################################################

def GameOn_Random():
    global nummoves, nummovestot
    nummoves = 0
    InitBoard()
    # PrintBoard()
    while cars[0][4] != (boardsize - 2) :
        AllPossibleMoves()
        ChooseRandomMove()
        # ChooseMovePrefRight()
        # PrintBoard()
        MoveCar()
        # PrintBoard()
        # time.sleep(.100)
        # VisualizeCars()
        nummoves += 1
        # if nummoves % 1000 == 0:
        #     stop = time.time() - start
        #     print 'Movenum: ', nummoves, "Time: ", stop, "msec"
        if nummoves > min(nummovestot):
            break
    if nummoves < min(nummovestot):
        nummovestot.append(nummoves)
        print 'EXIT!', nummoves, nummovestot

def GameOn_Random_Num(n):
    global nummovestot
    global k
    k = 0
    while k < n:
        GameOn_Random()
        k += 1

def GameOn_Algo():
    global nummoves
    start = time.time()
    InitBoard()
    i = 0
    while cars[0][4] != (boardsize - 2):
        ChooseCar()

def BreadthFirst():
    pass

def DepthFirst(depth):
    global nummoves, nummovestot
    nummoves = 0
    InitBoard()
    while cars[0][4] != (boardsize - 2) :
        AllPossibleMoves()
        ChooseRandomMove()
        movesmade.append(move)
        MoveCar()
        nummoves += 1
        if nummoves > depth:
            False
    print 'EXIT!', nummoves, nummovestot
######################################################################################

    # Visualisation
######################################################################################

def VisualizeCars():
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


    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
