# Rushhour
Solving a set of rushhourgames with algorithms.
Algorithms implemented: Random, BreadthFirstSearch
Partly implemented: DepthFirstSearch, Smart human thinking pattern

Rushhour.py provides the interface for selecting a script.

Use: rushhour.py [b] [a] [n]
b: board (possible entries 0 - 8)  
a: algorithm (possible: random, bfs, dfs, special) (special not implemented thoroughly)  
n: num, for random enter the number of times the script should be executed, for dfs give a maxdepth  


If no switches have been provided (so only using rushhour.py), a menu will be started, prompting the user to make the aforementioned decisions.


functions.py contains all the general helper functions and the sequences of these functions that make upp the algorithms
