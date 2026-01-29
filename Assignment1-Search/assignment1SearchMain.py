import heuristics
import romaniaDistances
import haversineHeuristic

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

    # To be used with the best first (greedy algorithm) and A* algorithm
    traingleInequalityHeuristic = heuristics.traingleInequalityHeuristics(startCity, endCity)
    haversineHeuristicValue = haversineHeuristic.haversine_StraightLine_Heuristic(startCity, endCity)

if __name__ == "__main__":
    main()