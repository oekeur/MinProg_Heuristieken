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

# initialize some vars
moves1 = {}       # dictionary: key=id, value=move, holds all moves right or up 
moves2 = {}       # dictionary: key=id, value=move, holds all moves left or down
move = []         # list with: car to move, to which y, x
archive =  set()  # set: value=hashedmatrix
cars = []         # list of list with ID, orientation, length, y and x
Rmatrix = [[]]    # List of list representing a matrix 
boardsize = 0     # integer to initialy build up an empty board
hashval = ""      # not really hashed, a string that depicts the position of each car
nummoves = 0      # number of moves done 

def InitBoard():
    global cars, Rmatrix, boardsize
    # open the board
    csvfile = open('board1.csv')
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
    Rmatrix = [['0' for x in range(boardsize)] for y in range(boardsize)]
    UpdateWholeBoard()

def PrintBoard():
    i = 0
    print "Boardmatrix:"
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
    print "Up/Left moves:", moves1
    print "Down/Right moves:", moves2
    print

def UpdateWholeBoard():
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


def isValidMove(x, y):
  """"
  Return True if the move is valid (on board and free)
  """

  if 0 <= x < boardsize and 0 <= y < boardsize and Rmatrix[y][x] == '0':
      return True
  else:
      return False

def PossibleMoves():
    i = 0
    for car in cars:
        global moves1, moves2
        if cars[i][1] == 'h':
            x = cars[i][4] - 1
            y = cars[i][3]
            if isValidMove(x,y):
                moves1[i] = [y,x]
            x = cars[i][4] + cars[i][2]
            y = cars[i][3]
            if isValidMove(x,y):
                x = cars[i][4] + 1
                moves2[i] = [y,x]
        else:
            y = cars[i][3] - 1
            x = cars[i][4]
            if isValidMove(x,y):
                moves1[i] = [y,x]
            y = cars[i][3] + cars[i][2]
            x = cars[i][4]
            if isValidMove(x,y):
                y = cars[i][3] + 1
                moves2[i] = [y,x]
        i += 1

def ChooseRandomMove():
    global move
    moveid = random.choice([moves1, moves2]).keys()[0]
    if moves1.get(moveid) is None:
        movexy = moves2.get(moveid)
    else:
        movexy = moves1.get(moveid)
    move = [moveid , movexy]

def MoveCar():
    global Rmatrix
    i = move[0] # list with move to make
    y = move[1][0]
    x = move[1][1]
    Rmatrix[cars[i][3]][cars[i][4]] = '0'
 # location of front is occupied at board
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

def GameOn():
    global nummoves
    InitBoard()
    start = time.time()
    while cars[0][4] != (boardsize - 2): # otther size board, include y
        PossibleMoves()
        ChooseRandomMove()
        while not EvaluateState:
            MoveCar
            print 'Already been here!'
        nummoves += 1
        if nummoves % 5000 == 0:
            stop = time.time() - start
            print 'Movenum: ', nummoves, "Time: ", stop, "msec"


# actual program sequence
#################################################################################################
GameOn()


# pre_init_time = time.time()
# InitBoard()
# post_init_time = time.time() - pre_init_time

# pre_calcmove_time = time.time()
# PossibleMoves()
# post_calcmove_time = time.time() - pre_calcmove_time

# pre_choose_time = time.time()
# ChooseRandomMove()
# post_choose_time = time.time() - pre_choose_time

# pre_deter_time = time.time()
# DetermineBoardState()
# post_deter_time = time.time() - pre_deter_time

# pre_move_time = time.time()
# MoveCar()
# post_move_time = time.time() - pre_move_time


# PrintBoard()
# PrintCars()
# PrintMoves()

# print "Boardinitialize:", post_init_time,  "msec"
# print "Movecalculate:", post_calcmove_time,  "msec"
# print "Determine:", post_deter_time,  "msec"
# print "Choosemove:", post_choose_time,  "msec"
# print "Move:", post_move_time,  "msec"

#################################################################################################





# set of board positions

# list of the eventual moves solving the puzzle