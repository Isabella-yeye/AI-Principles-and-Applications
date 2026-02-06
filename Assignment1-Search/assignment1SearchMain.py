import heuristics
import romaniaDistances
import breadthFirstSearch
import depthFirstSearch
import bestFirstSearch
import aStarSearch
import pathCostCalculator

def main():
    # Get the list of valid cities from the romaina_map
    validCities = list(romaniaDistances.romaina_map.keys())  

    print("Please enter the starting city: ")
    # Read user input for first city and remove leading/trailing whitespace
    startCity = input().strip() 
    startCity = startCity.title()  # Capitalize the first letter of each word
    # Loops until a city from the valid cities list is entered
    while startCity not in validCities:
        print(f"Error: '{startCity}' is not a valid city. Please enter a valid city from the following list:")
        print(", ".join(validCities))
        # Read user input for first city again and remove leading/trailing whitespace
        startCity = input().strip() 
        startCity = startCity.title()

    """
    Commented out due to assignment changes, but available to uncomment to change the end city from Bucharest
    
    print("\nPlease enter the ending city: ")
    # Read user input for second city and remove leading/trailing whitespace
    endCity = input().strip() 
    endCity = endCity.title()  # Capitalize the first letter of each word
    # Loops until a city from the valid cities list is entered
    while endCity not in validCities:
        print(f"Error: '{endCity}' is not a valid city. Please enter a valid city from the following list:")
        print(", ".join(validCities))
        # Read user input for first city again and remove leading/trailing whitespace
        endCity = input().strip()
        endCity = endCity.title()
        """
    endCity = "Bucharest"

    # To be used with the best first (greedy algorithm) and A* algorithm
    traingleInequalityHeuristic = heuristics.traingleInequalityHeuristics(endCity)
    haversineHeuristic = heuristics.haversineHeuristics(endCity)

    # Breadth First Search
    BFS = breadthFirstSearch.breadthFirstSearch(romaniaDistances.romaina_map, startCity, endCity)
    BFSCost = pathCostCalculator.pathCostCalculator(romaniaDistances.romaina_map, BFS)

    # Depth First Search
    DFS = depthFirstSearch.depthFirstSearch(startCity, endCity)
    DFSCost = pathCostCalculator.pathCostCalculator(romaniaDistances.romaina_map, DFS)

    # Best First Search (Greedy Algorithm)
    BFS_Greedy = bestFirstSearch.bestFirstSearch(romaniaDistances.romaina_map, traingleInequalityHeuristic, startCity, endCity) # Using Triangle Inequality Heuristic
    BFS_Greedy2 = bestFirstSearch.bestFirstSearch(romaniaDistances.romaina_map, haversineHeuristic, startCity, endCity) # Using Haversine Heuristic
    BFS_GreedyCost = pathCostCalculator.pathCostCalculator(romaniaDistances.romaina_map, BFS_Greedy)
    BFS_Greedy2Cost = pathCostCalculator.pathCostCalculator(romaniaDistances.romaina_map, BFS_Greedy2)

    # A* Search
    AStar = aStarSearch.aStarSearch(romaniaDistances.romaina_map, traingleInequalityHeuristic, startCity, endCity) # Using Triangle Inequality Heuristic
    AStar2 = aStarSearch.aStarSearch(romaniaDistances.romaina_map, haversineHeuristic, startCity, endCity) # Using Haversine Heuristic
    AStarCost = pathCostCalculator.pathCostCalculator(romaniaDistances.romaina_map, AStar)
    AStar2Cost = pathCostCalculator.pathCostCalculator(romaniaDistances.romaina_map, AStar2)

    # Print the results
    print(f"\nBreadth First Search path from {startCity} to {endCity}: {BFS}. \nThe path cost is {BFSCost}.")
    print(f"\nDepth First Search path from {startCity} to {endCity}: {DFS}. \nThe path cost is {DFSCost}.")
    print(f"\nBest First Search (Greedy Algorithm) path using Triangle Inequality Heuristic from {startCity} to {endCity}: {BFS_Greedy}. \nThe path cost is {BFS_GreedyCost}.")
    print(f"\nBest First Search (Greedy Algorithm) path using Haversine Heuristic from {startCity} to {endCity}: {BFS_Greedy2}. \nThe path cost is {BFS_Greedy2Cost}.")
    print(f"\nA* Search path using Triangle Ineqaulity Heuristic from {startCity} to {endCity}: {AStar}. \nThe path cost is {AStarCost}.")
    print(f"\nA* Search path using Haversine Heuristic from {startCity} to {endCity}: {AStar2}. \nThe path cost is {AStar2Cost}.")

if __name__ == "__main__":
    main()