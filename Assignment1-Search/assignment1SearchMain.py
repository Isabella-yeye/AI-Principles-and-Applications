import heuristics
import romaniaDistances
import breadthFirstSearch
import depthFirstSearch
import bestFirstSearch
import aStarSearch
import time
import csv

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

    # Breadth First Search
    BFSresults = []
    for i in range(0, 100):
        bfsStart = time.perf_counter()
        BFS = breadthFirstSearch.breadthFirstSearch(romaniaDistances.romaina_map, startCity, endCity)
        bfsEnd = time.perf_counter()
        elapsedTime = bfsEnd - bfsStart

        BFSresults.append({
            "Algorithm": "Breadth First Search",
            "Heuristic": "N/A",
            "Path": BFS["path"],
            "Path Length": BFS["pathLength"],
            "Nodes Expanded": BFS["nodesExpanded"],
            "Max Frontier Size": BFS["maxFrontierSize"],
            "Elapsed Time (seconds)": elapsedTime
        })

    # Average the results over 100 runs
    summary = []
    summary.append({
        "Algorithm": "Breadth First Search",
        "Heuristic": "N/A",
        "Path From First Run": BFSresults[0]["Path"],
        "Average Path Length": sum(result["Path Length"] for result in BFSresults) / len(BFSresults),
        "Average Nodes Expanded": sum(result["Nodes Expanded"] for result in BFSresults) / len(BFSresults),
        "Average Max Frontier Size": sum(result["Max Frontier Size"] for result in BFSresults) / len(BFSresults),
        "Average Elapsed Time (seconds)": sum(result["Elapsed Time (seconds)"] for result in BFSresults) / len(BFSresults)
    })

    # Depth First Search
    DFSResults = []
    for i in range(0, 100):
        dfsStart = time.perf_counter()
        DFS = depthFirstSearch.depthFirstSearch(startCity, endCity)
        dfsEnd = time.perf_counter()
        elapsedTime = dfsEnd - dfsStart

        DFSResults.append({
            "Algorithm": "Depth First Search",
            "Heuristic": "N/A",
            "Path": DFS["path"],
            "Path Length": DFS["pathLength"],
            "Nodes Expanded": DFS["nodesExpanded"],
            "Max Frontier Size": DFS["maxFrontierSize"],
            "Elapsed Time (seconds)": elapsedTime
        })

    summary.append({
        "Algorithm": "Depth First Search",
        "Heuristic": "N/A",
        "Path From First Run": DFSResults[0]["Path"],
        "Average Path Length": sum(result["Path Length"] for result in DFSResults) / len(DFSResults),
        "Average Nodes Expanded": sum(result["Nodes Expanded"] for result in DFSResults) / len(DFSResults),
        "Average Max Frontier Size": sum(result["Max Frontier Size"] for result in DFSResults) / len(DFSResults),
        "Average Elapsed Time (seconds)": sum(result["Elapsed Time (seconds)"] for result in DFSResults) / len(DFSResults)
    })
    

    # Best First Search (Greedy Algorithm) Triangle Inequality Heuristic
    BFS_Greedy_Results = []
    for i in range(0, 100):
        bfsGreedyStart = time.perf_counter()
        BFS_Greedy = bestFirstSearch.bestFirstSearch(romaniaDistances.romaina_map, traingleInequalityHeuristic, startCity, endCity)
        bfsGreedyEnd = time.perf_counter()
        elapsedTime = bfsGreedyEnd - bfsGreedyStart

        BFS_Greedy_Results.append({
            "Algorithm": "Best First Search (Greedy)",
            "Heuristic": "Triangle Inequality",
            "Path": BFS_Greedy["path"],
            "Path Length": BFS_Greedy["path_length"],
            "Nodes Expanded": BFS_Greedy["nodes_expanded"],
            "Max Frontier Size": BFS_Greedy["max_frontier_size"],
            "Elapsed Time (seconds)": elapsedTime
        })

    summary.append({
        "Algorithm": "Best First Search (Greedy)",
        "Heuristic": "Triangle Inequality",
        "Path From First Run": BFS_Greedy_Results[0]["Path"],
        "Average Path Length": sum(result["Path Length"] for result in BFS_Greedy_Results) / len(BFS_Greedy_Results),
        "Average Nodes Expanded": sum(result["Nodes Expanded"] for result in BFS_Greedy_Results) / len(BFS_Greedy_Results),
        "Average Max Frontier Size": sum(result["Max Frontier Size"] for result in BFS_Greedy_Results) / len(BFS_Greedy_Results),
        "Average Elapsed Time (seconds)": sum(result["Elapsed Time (seconds)"] for result in BFS_Greedy_Results) / len(BFS_Greedy_Results)
    })

    # Best First Search (Greedy Algorithm) Haversine Heuristic
    BFS_Greedy_Results = []
    for i in range(0, 100):
        bfsGreedyStart = time.perf_counter()
        BFS_Greedy = bestFirstSearch.bestFirstSearch(romaniaDistances.romaina_map, haversineHeuristic, startCity, endCity)
        bfsGreedyEnd = time.perf_counter()
        elapsedTime = bfsGreedyEnd - bfsGreedyStart

        BFS_Greedy_Results.append({
            "Algorithm": "Best First Search (Greedy)",
            "Heuristic": "Haversine",
            "Path": BFS_Greedy["path"],
            "Path Length": BFS_Greedy["path_length"],
            "Nodes Expanded": BFS_Greedy["nodes_expanded"],
            "Max Frontier Size": BFS_Greedy["max_frontier_size"],
            "Elapsed Time (seconds)": elapsedTime
        })

    summary.append({
        "Algorithm": "Best First Search (Greedy)",
        "Heuristic": "Haversine",
        "Path From First Run": BFS_Greedy_Results[0]["Path"],
        "Average Path Length": sum(result["Path Length"] for result in BFS_Greedy_Results) / len(BFS_Greedy_Results),
        "Average Nodes Expanded": sum(result["Nodes Expanded"] for result in BFS_Greedy_Results) / len(BFS_Greedy_Results),
        "Average Max Frontier Size": sum(result["Max Frontier Size"] for result in BFS_Greedy_Results) / len(BFS_Greedy_Results),
        "Average Elapsed Time (seconds)": sum(result["Elapsed Time (seconds)"] for result in BFS_Greedy_Results) / len(BFS_Greedy_Results)
    })

    # A* Search Triangle Inequality Heuristic
    AStarResults = []
    for i in range(0, 100):
        aStarStart = time.perf_counter()
        AStar = aStarSearch.aStarSearch(romaniaDistances.romaina_map, traingleInequalityHeuristic, startCity, endCity)
        aStarEnd = time.perf_counter()
        elapsedTime = aStarEnd - aStarStart

        AStarResults.append({
            "Algorithm": "A* Search",
            "Heuristic": "Triangle Inequality",
            "Path": AStar["path"],
            "Path Length": AStar["path_length"],
            "Nodes Expanded": AStar["nodes_expanded"],
            "Max Frontier Size": AStar["max_frontier_size"],
            "Elapsed Time (seconds)": elapsedTime
        })

    summary.append({
        "Algorithm": "A* Search",
        "Heuristic": "Triangle Inequality",
        "Path From First Run": AStarResults[0]["Path"],
        "Average Path Length": sum(result["Path Length"] for result in AStarResults) / len(AStarResults),
        "Average Nodes Expanded": sum(result["Nodes Expanded"] for result in AStarResults) / len(AStarResults),
        "Average Max Frontier Size": sum(result["Max Frontier Size"] for result in AStarResults) / len(AStarResults),
        "Average Elapsed Time (seconds)": sum(result["Elapsed Time (seconds)"] for result in AStarResults) / len(AStarResults)
    })

    # A* Search Haversine Heuristic
    AStarResults = []
    for i in range(0, 100):
        aStarStart = time.perf_counter()
        AStar = aStarSearch.aStarSearch(romaniaDistances.romaina_map, haversineHeuristic, startCity, endCity)
        aStarEnd = time.perf_counter()
        elapsedTime = aStarEnd - aStarStart

        AStarResults.append({
            "Algorithm": "A* Search",
            "Heuristic": "Haversine Heuristic",
            "Path": AStar["path"],
            "Path Length": AStar["path_length"],
            "Nodes Expanded": AStar["nodes_expanded"],
            "Max Frontier Size": AStar["max_frontier_size"],
            "Elapsed Time (seconds)": elapsedTime
        })

    summary.append({
        "Algorithm": "A* Search",
        "Heuristic": "Haversine Heuristic",
        "Path From First Run": AStarResults[0]["Path"],
        "Average Path Length": sum(result["Path Length"] for result in AStarResults) / len(AStarResults),
        "Average Nodes Expanded": sum(result["Nodes Expanded"] for result in AStarResults) / len(AStarResults),
        "Average Max Frontier Size": sum(result["Max Frontier Size"] for result in AStarResults) / len(AStarResults),
        "Average Elapsed Time (seconds)": sum(result["Elapsed Time (seconds)"] for result in AStarResults) / len(AStarResults)
    })

    # Export to CSVs
    with open("algorithm_results.csv", "w", newline="") as csvfile:
        fieldnames = ["Algorithm", "Heuristic", "Average Elapsed Time (seconds)", "Average Nodes Expanded", "Average Max Frontier Size", "Average Path Length", "Path From First Run"]
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

if __name__ == "__main__":
    main()