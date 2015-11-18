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
# import random # to make automated random moves

# initialize some vars
moves = {}        # dictionary: key=id, value=move
archive =  set()  # set: value=hashedmatrix
cars = []         # list of list with ID, orientation, length, y and x
Rmatrix = [[]]    # List of list representing a matrix 
boardsize = 0     # integer to initialy build up an empty board
hashval = ""      # not really hashed, a string that depicts the position of each car
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

def PrintCars():
    i = 0
    print "List of cars:"
    for entry in cars:
        print cars[i]
        i += 1

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
  print 
  if Rmatrix[y][x] == '0' and 0 <= x < boardsize and 0 <= y < boardsize:
      return True
  else:
      return False

def EvaluateState():
    DetermineBoardState()
    if hashval not in archive:
        archive.add(hashval)

        return True
    else:
        return False

def DetermineBoardState():
    global hashval
    hashval = ""
    i = 0
    for column in Rmatrix:
        j = 0
        for row in column:
            hashval += Rmatrix[j][i]
            j += 1
        i += 1


# actual program sequence
#################################################################################################
preinit = time.time() * 1000
InitBoard()
postinit = time.time() * 1000 - preinit
# print "Boardinitialize:", postinit,  "msec"

# PrintCars()
# PrintBoard()
# test()


#################################################################################################


# def UpdateCars():


# def PossibleMoves():
#     for car in cars:
#         i = 0
#         if car[i][1] == 'h':
#             x = car[i][4] - 1
#             y = car[i][3]
#             if isValidMove(x,y):
#                 moves.append(car[i][0], x,y)
#             x = car[i][4] + car[i][2]
#             y = car[i][3]
#             if isValidMove(x,y):
#                 moves.append()
#         else:
#             y = car[i][3] - 1
#             x = car[i][4]
#             if isValidMove(x,y):
#                 moves.append()
#             y = car[i][3] + car[i][2]
#             x = car[i][4]
#             if isValidMove(x,y):
#                 moves.append()
#         i += 1
#     return moves




# def randomMove(moves)
#     move = random.choice(moves)
#     return move

# set of board positions

# list of the eventual moves solving the puzzle