import functions
import time



#Automated moves
###################################################
functions.GameOn_Random() # random moves untill endsituation is reached

# functions.GameOn_Num(5) # make n moves, or untill endsituation reached
###################################################



# Separate functions (for testing purposes)
###################################################
# functions.test()

# pre_init_time = time.time()
# functions.InitBoard()
# post_init_time = time.time() - pre_init_time

# pre_calcmove_time = time.time()
# functions.AllPossibleMoves()
# post_calcmove_time = time.time() - pre_calcmove_time

# pre_vis_time = time.time()
# functions.VisualizeCars()
# post_vis_time = time.time() - pre_vis_time

# functions.PrintBoard()
# functions.PrintCars()

# pre_choose_time = time.time()
# functions.ChooseRandomMove()
# post_choose_time = time.time() - pre_choose_time

# functions.PrintMoves()

# pre_deter_time = time.time()
# functions.DetermineBoardState()
# post_deter_time = time.time() - pre_deter_time

# pre_move_time = time.time()
# functions.MoveCar()
# post_move_time = time.time() - pre_move_time

# functions.PrintBoard()


# functions.PrintCars()

# print "Boardinitialize:", post_init_time,  "msec"
# print "Movecalculate:", post_calcmove_time,  "msec"
# print "Determine:", post_deter_time,  "msec"
# print "Choosemove:", post_choose_time,  "msec"
# print "Move:", post_move_time,  "msec"
# print "Visualize:", post_vis_time,  "msec"