# An implementation of a game of rushhour
# Ultimate goal is to get a algorithm (BFS probably) get to solve at least 6 given puzzles
#
# Names: Kyra Kieskamp & Oscar Keur
# Stud.no.: 10099727 & 11122102
#
# Version: 0.1
# Changes: Skeleton to import a board an display it

# import time # to calculate time needed
# import pygame # to use visuals
# import sys # to use argv
import csv # to use csv.reader
# import random # to make automated random moves

# initialize some vars
moves = {}
cars = []
Rmatrix = [[]]
boardsize = 0
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


def PrintBoard():
    i = 0
    print "Boardmatrix:"
    for row in Rmatrix:
        print Rmatrix[i]
        i += 1

def PrintCars():
    i = 0
    print "List of cars:"
    for entry in cars:
        print cars[i]
        i += 1

def UpdateBoard():
    i = 0
    # for each car
    for car in cars:
        # location of front is occupied at board
        Rmatrix[cars[i][3]][cars[i][4]] = cars[i][0]
        # if orientation is horizontal update the tile to the left as occupied
        if cars[i][1] == 'h':
            Rmatrix[cars[i][3] + 1][cars[i][4]] = cars[i][0]
            # if the length of the car is 3, also occupy the next tile
            if cars[i][2] == 3:
                Rmatrix[cars[i][3] + 2][cars[i][4]] = cars[i][0]
        # same for vertical orientation
        else:
             Rmatrix[cars[i][3]][cars[i][4] + 1] = cars[i][0]
             if cars[i][2] == 3:
                Rmatrix[cars[i][3]][cars[i][4] + 2] = cars[i][0]
        i += 1

InitBoard()
PrintCars()
PrintBoard()
UpdateBoard()
PrintBoard()

# class Position(object):
#     """
#     A Position represents a location in a two-dimensional room.
#     """
#     def __init__(self, x, y, dir, size):
#         """
#         Initializes a position with coordinates (x, y).
#         """
#         self.x = x
#         self.y = y
#     def getX(self):
#         return self.x
#     def getY(self):
#         return self.y
#     def getNewPosition(self, dir, size):
#         """
#         Computes and returns the new Position with this object as the current position

#         Does NOT test whether the returned position fits inside the room.

#         angle: float representing angle in degrees, 0 <= angle < 360
#         speed: positive float representing speed

#         Returns: a Position object representing the new position.
#         """
#         if dir:
#             old = self.getX()
#             new_x = old - 1
#             new_y = self.getY()
#         else:
#             old = self.getY()
#             new_y = old - 1
#             new_x = self.getX()
#         return Position(new_x, new_y))

# def isValidMove(self, pos):
#     """"
#     Return True if the move is valid (on board and free)

#     pos: a Position object.
#     """
#   if self.pos == "free" and (0 <= pos.getX() < self.width and 0 <= pos.getY() <= self.height):
#       return True
#   else:
#       return False


# class Car(object):
#     """
#     Represents a Car on a particular board.

#     At all times the Car has a particular position and direction in the board.
#     The Car also has a fixed speed.

#     Subclasses of Car should provide movement strategies by implementing
#     updatePositionAndClean(), which simulates a single time-step.
#     """
#     def __init__(self, board):
#         """
#         Initializes a car on the specified board.

#         board:  a Board object.
#         """
#         self.board = board
#         self.id = # from csvfile
#         self.pos = # implement from the provided csv file with initial car positions
#         self.dir = # make a boolean from direction (horizontal == True, vertical == False)
#         self.size = # from file


#     def getCarPosition(self):
#         """
#         Return the position of the Car.

#         returns: a Position object giving the Car's position.
#         """
#         return self.pos

#     def getCarDirection(self):
#         """
#         Return the direction of the Car.

#         returns: horizontal or vertical
#         """
#         return self.dir

#     def setCarPosition(self, position):
#         """
#         Set the position of the Car to POSITION.

#         position: a Position object.
#         """
#         self.pos = position

#     def updatePosition(self):
#             newPos = self.getNewPosition(self.dir, self.size)

#             if isValidMove(newPos):
#                 moves.append{}

#             if dir:
#                 newPos.x += size + 1
#             else:
#                 newPos.y += size + 1

#             if isValidMove(newPos):
#                 moves.append{}



# class TargetCar(Car):
#     """ Docstring for the targetcar  """

#     def checkEnd():
#         if getNewPosition == "exit":
#             exit(0)




# def PossibleMoves():
#   return moves

# def randomMove(moves)
#     move = random.choice(moves)
#     return move
