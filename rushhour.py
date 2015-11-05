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

# moves = []

class Board(object):
	"""docstring for Board"""


class Car(object):
	"""docstring for Car"""


def LoadBoard(rushhourfile):
	try:
		f = open(rushhourfile)
	except IOERROR as e:
		print "Cannot open ", rushhourfile

# def DisplayBoard():
# 	pass

# def UpdateBoard():
# 	pass

# def PossibleMoves():
# 	return moves