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
import csv
import random

moves = {}


class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y, dir, size):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, dir, size):
        """
        Computes and returns the new Position with this object as the current position

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        if dir:
            old = self.getX()
            new_x = old - 1
            new_y = self.getY()
        else:
            old = self.getY()
            new_y = old - 1
            new_x = self.getX()
        return Position(new_x, new_y))

class Board(object):
	"""docstring for Board"""


	def isValidMove(self, pos):
        """"
        Return True if the move is valid (on board and free)

        pos: a Position object.
        """
		if self.pos == "free" and (0 <= pos.getX() < self.width and 0 <= pos.getY() <= self.height):
			return True
		else:
			return False


# import csv file
import csv
with open('ROpositions.csv') as csvfile:
reader = csv.DictReader(csvfile)
for row in reader:
    # create array in which positions are imported
    # array = row['something'], row['something']

class Car(object):
    """
    Represents a Car on a particular board.

    At all times the Car has a particular position and direction in the board.
    The Car also has a fixed speed.

    Subclasses of Car should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, board):
        """
        Initializes a car on the specified board.

        board:  a Board object.
        """
        self.board = board
        self.id = # from csvfile
        self.pos = # implement from the provided csv file with initial car positions
        self.dir = # make a boolean from direction (horizontal == True, vertical == False)
        self.size = # from file


    def getCarPosition(self):
        """
        Return the position of the Car.

        returns: a Position object giving the Car's position.
        """
        return self.pos

    def getCarDirection(self):
        """
        Return the direction of the Car.

        returns: horizontal or vertical
        """
        return self.dir

    def setCarPosition(self, position):
        """
        Set the position of the Car to POSITION.

        position: a Position object.
        """
        self.pos = position

    def updatePosition(self):
            newPos = self.getNewPosition(self.dir, self.size)

            if isValidMove(newPos):
                moves.append{}

            if dir:
                newPos.x += size + 1
            else:
                newPos.y += size + 1

            if isValidMove(newPos):
                moves.append{}



class TargetCar(Car):
    """ Docstring for the targetcar  """

    def checkEnd():
        if getNewPosition == "exit":
            exit(0)
    


def LoadBoard(rushhourfile):
	try:
		f = open(rushhourfile)
	except IOERROR as e:
		print "Cannot open ", rushhourfile
		break
	board = csv.reader(rushhourfile, dialect='excel', delimiter=';')
	while board.readlines():
        for y in ypos:
            for x in xpos:





def DisplayBoard():
    for x in :
        pass

# def UpdateBoard():
# 	pass

def PossibleMoves():
	return moves

def randomMove(moves)
    move = random.choice(moves)
    return move 
