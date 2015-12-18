import functions
import time
import sys
import csv

algorithmlist = ["EXIT", "RANDOM", "BFS", "DFS", "SPECIAL"]

def main():
	if len(sys.argv) == 1:
		while True:
			boardchoice = ChooseBoard()
			algorithmchoice, num = ChooseAlgorithm()	
			break
	else:
		boardchoice, algorithmchoice, num = CommandLineArguments()
	print "Board:", boardchoice, algorithmlist[algorithmchoice], "Num:", num
	ExecuteAlgorithm(boardchoice, algorithmchoice, num)

def CommandLineArguments():
	try:
		boardchoice = int(sys.argv[1])
	except ValueError:
		print("Sorry, I didn't understand that. Please choose 0-7")
		sys.exit(1)
	except NameError:
		print("Sorry, I didn't understand that. Please choose 0-7")
		sys.exit(1)
	if boardchoice < 0 or boardchoice > 8:
			print "That's not a valid choice.. board"
			sys.exit(1)
	#############################################################
	try:
		algorithmchoice = str(sys.argv[2]).upper()
	except ValueError:
		print("Sorry, I didn't understand that. Please choose bfs, dfs, random or special")
		sys.exit(1)
	except NameError:
		print("Sorry, I didn't understand that. Please choose bfs, dfs, random or special")
		sys.exit(1)
	if algorithmchoice not in ["BFS", "DFS", "RANDOM", "SPECIAL"]:
			print "That's not a valid choice.. Please choose bfs, dfs, random or special"
			sys.exit(1)
	###############################################################
	if algorithmchoice == "RANDOM" or algorithmchoice == "DFS":
		try:
			num = int(sys.argv[3])
		except ValueError:
			print("Sorry, I didn't understand that.")
			sys.exit(1)
		except NameError:
			print("Sorry, I didn't understand that.")
			sys.exit(1)
		if num <= 0:
			print "Funny you..."
			sys.exit(1)
	else:
		num = 0
	algorithmchoice = algorithmlist.index(algorithmchoice)
	return (boardchoice, algorithmchoice, num)

def ChooseBoard():
	while True:
		try:
			print "Please choose a board"
			print "	  0: Exit program"
			print "	1-3: 6X6   Boards"
			print "	4-6: 9X9   Boards"
			print "	  7: 12X12 Board"
			print "	  8: Testboard"
			print ""
			boardchoice=int(input("Which board would you like to solve? "))
		except ValueError:
			print("Sorry, I didn't understand that. Please choose 0-7")
			continue
		except NameError:
			print("Sorry, I didn't understand that. Please choose 0-7")
			continue
		except SyntaxError:
			print("Sorry, I didn't understand that. Please choose 0-7")
			continue
		if boardchoice < 0 or boardchoice > 8:
				print "That's not a valid choice.."
				continue 
		elif boardchoice == 0:
			sys.exit(0)
		else:
			print ""
			return boardchoice		

def ChooseAlgorithm():
	while True:
		try:
			print "Please choose an algorithm"
			print "	0: Exit program"
			print "	1: Random Search"
			print "	2: Breadth First Search"
			print "	3: Depth First Search"
			# print "	4: Our own humanthinkinglike algorithm" # not implemented yet
			print ""
			algorithmchoice=int(input("Which algorithm would you like to execute? "))
		except ValueError:
			print("Sorry, I didn't understand that. Please choose 0-3")
			continue
		except NameError:
			print("Sorry, I didn't understand that. Please choose 0-3")
			continue
		except SyntaxError:
			print("Sorry, I didn't understand that. Please choose 0-3")
			continue
		if algorithmchoice < 0 or algorithmchoice > 3:
			print "That's not a valid choice.."
			continue 
		elif algorithmchoice == 0:
			sys.exit(0)
		elif algorithmchoice == 1:
			try:
				num =int(input("How many times should we do a random search? "))
			except ValueError:
				print("Sorry, I didn't understand that.")
				sys.exit(1)
			except NameError:
				print("Sorry, I didn't understand that.")
				sys.exit(1)
			except SyntaxError:
				print("Sorry, I didn't understand that.")
				continue
			if num <= 0:
				print "Funny you..."
				sys.exit(1)
		elif algorithmchoice == 3:
			try:
				num =int(input("How deep should we search into the tree? "))
			except ValueError:
				print("Sorry, I didn't understand that.")
				sys.exit(1)
			except NameError:
				print("Sorry, I didn't understand that.")
				sys.exit(1)
			except SyntaxError:
				print("Sorry, I didn't understand that.")
				continue
			if num <= 0:
				print "Funny you..."
				sys.exit(1)
		else:
			num = 0
		print ""
		return (algorithmchoice, num)

def ExecuteAlgorithm(boardchoice, algorithmchoice, num):
	if algorithmchoice == 0:
		sys.exit(0)
	elif algorithmchoice == 1:
		try:
			functions.GameOn_Random_Num(boardchoice, num) # random moves untill endsituation is reached, num times
		except KeyboardInterrupt:
			WriteResults(boardchoice, algorithmchoice)
			sys.exit(0)
	elif algorithmchoice == 2:
		try:
			functions.BreadthFirst(boardchoice) # Breadth First Search
			with open('results.csv', 'ab') as csvfile:
				writer = csv.writer(csvfile, delimiter=',',
				quotechar='\"', quoting=csv.QUOTE_MINIMAL)
				writer.writerow([boardchoice, algorithmlist[algorithmchoice],  1,   functions.nummoves])
		except KeyboardInterrupt:
			with open('results.csv', 'ab') as csvfile:
				writer = csv.writer(csvfile, delimiter=',',
				quotechar='\"', quoting=csv.QUOTE_MINIMAL)
				writer.writerow([boardchoice, "DFS", len(movesmade), 1, iteration])
			sys.exit(0)
	elif algorithmchoice == 3:
		try:
			functions.DepthFirst(boardchoice, num) # Breadth First Search
			WriteResults(boardchoice, algorithmchoice)

		except KeyboardInterrupt:
			WriteResults(boardchoice, algorithmchoice)
			sys.exit(0)
	# elif algorithmchoice == 4:
	# 	# try:
		# 	functions.GameOn_Algo(boardchoice, num) # Breadth First Search
		# except KeyboardInterrupt:
		# 	WriteResults(boardchoice, algorithmchoice)
		# 	sys.exit(0)

def WriteResults(boardchoice, algorithmchoice):
   with open('results.csv', 'ab') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                                quotechar='\"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([boardchoice, algorithmlist[algorithmchoice], len(functions.nummovestot) - 1,   min(functions.nummovestot)])

if __name__ == '__main__':
  main()



###################################################

# cars = functions.InitBoard(sys.argv[1])
# print cars
# functions.BreadthFirst(8)
# Separate functions (for testing purposes)
###################################################
# functions.test()

# functions.InitBoard()

# functions.AllPossibleMoves()


#functions.VisualizeCars()


# functions.PrintBoard()
# functions.PrintCars()

# functions.ChooseRandomMove()

# functions.PrintMoves()

# functions.DetermineBoardState()

# functions.MoveCar()

# functions.PrintBoard()

# functions.BreadthFirst(1)
# functions.PrintCars()

