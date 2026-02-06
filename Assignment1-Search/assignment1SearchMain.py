import heuristics
import romaniaDistances
import breadthFirstSearch
import depthFirstSearch
import bestFirstSearch
import aStarSearch
import pathCostCalculator
import time
import csv

def main():
    summary = []
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

    heuristicsTimes = []
    # To be used with the best first (greedy algorithm) and A* algorithm
    TIHStart = time.perf_counter()
    traingleInequalityHeuristic = heuristics.traingleInequalityHeuristics(endCity)
    TIHEnd = time.perf_counter()
    elapsedTimeTIH = TIHEnd - TIHStart
    heuristicsTimes.append({
        "Heuristic": "Triangle Inequality",
        "Elapsed Time (seconds)": elapsedTimeTIH
        })

    HHStart = time.perf_counter()
    haversineHeuristic = heuristics.haversineHeuristics(endCity)
    HHEnd = time.perf_counter()
    elapsedTimeHH = HHEnd - HHStart
    heuristicsTimes.append({
        "Heuristic": "Haversine",
        "Elapsed Time (seconds)": elapsedTimeHH
        })

    BFSResults = []
    # Breadth First Search
    for i in range (0, 100):
        bfsStart = time.perf_counter()
        BFS = breadthFirstSearch.breadthFirstSearch(romaniaDistances.romaina_map, startCity, endCity)
        bfsEnd = time.perf_counter()
        elapsedTime = bfsEnd - bfsStart
        BFSResults.append(elapsedTime)
    summary.append({
        "Algorithm": "Breadth First Search",
        "Average Elapsed Time (seconds)": sum(result for result in BFSResults) / len(BFSResults)
        })
    BFSCost = pathCostCalculator.pathCostCalculator(romaniaDistances.romaina_map, BFS)

    DFSResults = []
    # Depth First Search
    for i in range (0, 100):
        dfsStart = time.perf_counter()
        DFS = depthFirstSearch.depthFirstSearch(startCity, endCity)
        dfsEnd = time.perf_counter()
        elapsedTime = dfsEnd - dfsStart
        DFSResults.append(elapsedTime)
    summary.append({
        "Algorithm": "Depth First Search",
        "Average Elapsed Time (seconds)": sum(result for result in DFSResults) / len(DFSResults)
        })
    DFSCost = pathCostCalculator.pathCostCalculator(romaniaDistances.romaina_map, DFS)

    greedyResultTriangle = []
    greedyResultHaversine = []
    # Best First Search (Greedy Algorithm)
    for i in range (0, 100):
        greedyStart = time.perf_counter()
        BFS_Greedy = bestFirstSearch.bestFirstSearch(romaniaDistances.romaina_map, traingleInequalityHeuristic, startCity, endCity) # Using Triangle Inequality Heuristic
        greedyEnd = time.perf_counter()
        elapsedTime = greedyEnd - greedyStart
        greedyResultTriangle.append(elapsedTime)

        greedy2Start = time.perf_counter()
        BFS_Greedy2 = bestFirstSearch.bestFirstSearch(romaniaDistances.romaina_map, haversineHeuristic, startCity, endCity) # Using Haversine Heuristic
        greedy2End = time.perf_counter()
        elapsedTime = greedy2End - greedy2Start
        greedyResultHaversine.append(elapsedTime)
    summary.append({
    "Algorithm": "Best First Search (Greedy Algorithm) with Triangle Inequality Heuristics",
    "Average Elapsed Time (seconds)": sum(result for result in greedyResultTriangle) / len(greedyResultTriangle)
    })
    summary.append({
    "Algorithm": "Best First Search (Greedy Algorithm) with Haversine Heuristics",
    "Average Elapsed Time (seconds)": sum(result for result in greedyResultHaversine) / len(greedyResultHaversine)
    })
    BFS_GreedyCost = pathCostCalculator.pathCostCalculator(romaniaDistances.romaina_map, BFS_Greedy)
    BFS_Greedy2Cost = pathCostCalculator.pathCostCalculator(romaniaDistances.romaina_map, BFS_Greedy2)

    aStarResultTriangle = []
    aStarResultHaversine = []
    # A* Search
    for i in range(0, 100):
        aStarStart = time.perf_counter()
        AStar = aStarSearch.aStarSearch(romaniaDistances.romaina_map, traingleInequalityHeuristic, startCity, endCity) # Using Triangle Inequality Heuristic
        aStarEnd = time.perf_counter()
        elapsedTime = aStarEnd - aStarStart
        aStarResultTriangle.append(elapsedTime)
        
        aStar2Start = time.perf_counter()
        AStar2 = aStarSearch.aStarSearch(romaniaDistances.romaina_map, haversineHeuristic, startCity, endCity) # Using Haversine Heuristic
        aStar2End = time.perf_counter()
        elapsedTime = aStar2End - aStar2Start
        aStarResultHaversine.append(elapsedTime)
    summary.append({
    "Algorithm": "A* Search with Triangle Inequality Heuristics",
    "Average Elapsed Time (seconds)": sum(result for result in aStarResultTriangle) / len(aStarResultTriangle)
    })
    summary.append({
    "Algorithm": "A* Search with Haversine Heuristics",
    "Average Elapsed Time (seconds)": sum(result for result in aStarResultHaversine) / len(aStarResultHaversine)
    })
    AStarCost = pathCostCalculator.pathCostCalculator(romaniaDistances.romaina_map, AStar)
    AStar2Cost = pathCostCalculator.pathCostCalculator(romaniaDistances.romaina_map, AStar2)

    # Export to CSVs
    with open("algorithm_results.csv", "w", newline="") as csvfile:
        fieldnames = ["Algorithm", "Average Elapsed Time (seconds)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Write column headers
        for r in summary:
            writer.writerow(r)

    print("\nCSV file saved as algorithm_results.csv")

    with open("heuristics_results.csv", "w", newline="") as csvfile:
        fieldnames = ["Heuristic", "Elapsed Time (seconds)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Write column headers
        for r in heuristicsTimes:
            writer.writerow(r)

    print("\nCSV file saved as heuristics_results.csv")

    # Print the results
    print(f"\nBreadth First Search path from {startCity} to {endCity}: {BFS}. \nThe path cost is {BFSCost}.")
    print(f"\nDepth First Search path from {startCity} to {endCity}: {DFS}. \nThe path cost is {DFSCost}.")
    print(f"\nBest First Search (Greedy Algorithm) path using Triangle Inequality Heuristic from {startCity} to {endCity}: {BFS_Greedy}. \nThe path cost is {BFS_GreedyCost}.")
    print(f"\nBest First Search (Greedy Algorithm) path using Haversine Heuristic from {startCity} to {endCity}: {BFS_Greedy2}. \nThe path cost is {BFS_Greedy2Cost}.")
    print(f"\nA* Search path using Triangle Ineqaulity Heuristic from {startCity} to {endCity}: {AStar}. \nThe path cost is {AStarCost}.")
    print(f"\nA* Search path using Haversine Heuristic from {startCity} to {endCity}: {AStar2}. \nThe path cost is {AStar2Cost}.")

if __name__ == "__main__":
    main()