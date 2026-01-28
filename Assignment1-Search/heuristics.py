# Two different ways to calculate heuristics for best first (greedy) algorithm and A* search algorithm
import math
import mapOfRomania

# Triangle inequality heuristic
# TODO
# MAKE SURE TO CHECK IN MAIN IF THE CITY EXISTS BEFORE SENDING IT HERE
def traingleInequalityHeuristics(start, end):
    # If Bucharest is the goal, the straight line distance (SLD) is already known
    if end == "Bucharest":
        return mapOfRomania.SLD_Bucharest[start] # Returns 0 because the SLD to Bucharest from Bucharest is 0
    # Estimates the SLD using Bucharest as the intermediate city
    else:
        # Returns the absolute value of the start to Bucharest minus the end to Bucharest
        return abs(mapOfRomania.SLD_Bucharest[start] - mapOfRomania.SLD_Bucharest[end]) 