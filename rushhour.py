# An implementation of a game of rushhour
# Ultimate goal is to get a algorithm (BFS probably) get to solve at least 6 given puzzles
#
# Names: Kyra Kieskamp & Oscar Keur
# Stud.no.: ???????? & 11122102
#
# Version: 0.1
# Changes: Skeleton to import a board an display it

# import time # to calculate time needed
# import pygame # to use visuals
# import sys # to use argv
import csv

# moves = []

class Board(object):
	"""docstring for Board"""



    def isPositionOnBoard(self, pos):
	    """
	    Return True if pos is on the board.

	    pos: a Position object.
	    returns: True if pos is on the board, False otherwise.
	    """
	    if (0 <= pos.getX() < self.width and 0 <= pos.getY() <= self.height):
	        return True
	    else:
	        return False

	def isNotOccupied(self, pos):
		if self.pos = " "
			return True
		else:
			return False

	def isValidMove():
		if isNotOccupied(pos) and isPositionOnBoard():
			return True
		else:
			return False
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
        self.pos = n
        self.dir = 

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

    def setCarDirection(self, direction):
        """
        Set the direction of the Car to DIRECTION.

        direction: horizontal or vertical
        """
        self.dir = direction

class TargetCar(Car):
    """ Docstring for the targetcar  """
    def updatePosition(self):
        inroom = False
        while inroom == False:
            newPos = self.getNewPosition(self.getCarDirection, self.speed)
            if isPositionOnBoard(newPos):
                self.pos = newPos
                inroom = True
            else:
                self.setCarDirection = random.randint(0,360)


def LoadBoard(rushhourfile):
	try:
		f = open(rushhourfile)
	except IOERROR as e:
		print "Cannot open ", rushhourfile
		break
	board = csv.reader(rushhourfile, dialect='excel', delimiter=';')
	while board.readlines():
		

# def DisplayBoard():
# 	pass

# def UpdateBoard():
# 	pass

# def PossibleMoves():
# 	return moves