# Implementation for a function to calculate the path cost
# This is seperate from the searches for readiability and to reduce issues with bugs

def pathCostCalculator(graph, path):
    # Set path cost to 0
    cost = 0

    for i in range(len(path) - 1):
        currentCity = path[i] # Get the current city from the path
        nextCity = path[i + 1] # Get the next city after the current city from the path

        # Look for the edge to get the weight (cost)
        for neighbor, weight in graph[currentCity]:
            # If the neighbor is the next city then add the weight to the cost
            if neighbor == nextCity:
                cost += weight
                break

    # Return the total path cost
    return cost