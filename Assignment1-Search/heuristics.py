# Two different ways to calculate heuristics for best first (greedy) algorithm and A* search algorithm
import math

# Straight Line Distance (SLD) to Bucharest for each city from the lecture slides
SLD_Bucharest = {
    "Arad": 366,
    "Zerind": 374,
    "Oradea": 380,
    "Sibiu": 253,
    "Timisoara": 329,
    "Lugoj": 244,
    "Mehadia": 241,
    "Drobeta": 242,
    "Craiova": 160,
    "Rimnicu Vilcea": 193,
    "Fagaras": 176,
    "Pitesti": 100,
    "Bucharest": 0,
    "Giurgiu": 77,
    "Urziceni": 80,
    "Hirsova": 151,
    "Eforie": 161,
    "Vaslui": 199,
    "Iasi": 226,
    "Neamt": 234
    }

# Triangle inequality heuristic
def traingleInequalityHeuristics(end):
    # Initialize an empty heuristic table to store cities and distances
    heuristicTable = {}

    # Loop through each city in the straight-line distance from Bucharest
    for city in SLD_Bucharest:
        # If the end city is Bucharest, use the straight-line distance directly
        if end == "Bucharest":
            heuristicTable[city] = SLD_Bucharest[city]

        # Otherwise, calculate the heuristic using the triangle inequality
        else:
            heuristicTable[city] = abs(SLD_Bucharest[city] - SLD_Bucharest[end])

    # Return the completed heuristic table to use in search algorithms
    return heuristicTable