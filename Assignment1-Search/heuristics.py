# Two different ways to calculate heuristics for best first (greedy) algorithm and A* search algorithm
import math

#haversineHeuristic = heuristics.haversineHeuristics(endCity)

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


# Heuristic to calculate straight line distance (km) using implementation of Haversine
# formula based on equation from https://www.movable-type.co.uk/scripts/latlong.html
# DD Coordinates taken from database.earth (https://database.earth/countries/romania/cities), 

# dictionary of selected city coordinates by name and (lat, lon)
romanina_city_coordinates = {
    "Arad":  (46.18333, 21.31667),
    "Zerind": (46.61667,21.51667),
    "Oradea": (47.05353, 21.93633),
    "Sibiu": (45.79383, 24.13533),
    "Timisoara": (45.75641, 21.22974),
    "Lugoj": (45.68861, 21.90306),
    "Mehadia": (44.90083, 22.36694),
    "Drobeta": (44.62693, 22.65288),
    "Craiova": (44.31943, 23.80875),
    "Rimnicu Vilcea": (45.09448, 24.35215), #Ramnicu Valcea
    "Fagaras": (45.84098, 24.97348),
    "Pitesti": (44.85782, 24.87133),
    "Bucharest": (44.43225, 26.10626),
    "Giurgiu": (43.88664, 25.9627),
    "Urziceni": (44.71842, 26.64187),
    "Hirsova": (44.68555, 27.95009), #Harsova
    "Eforie": (44.0653, 28.63211), # Eforie Nord (Eforie south is really close by)
    "Vaslui": (46.64683, 27.73872),
    "Iasi": (47.16184, 27.58451),
    "Neamt": (46.92336, 26.3738) #Municipiul Piatra-Neamt closest county to neamt coords from google maps
}

def haversineHeuristics(end: str):
    """Apply Haversine Formula to calculate distance between two cities based
       on DD coordinates listed in dictionary of Romanian cities listed above

       Args: 
            end (str): last city in search

        Returns: 
            haversineTable (float): table of straightline distances between cities and endpoint
     """
    #const value for radius of Earth
    haversineTable={}
    R = 6371
    # get coordinates for end city
    latEnd, lonEnd = (romanina_city_coordinates[end])
    for city in romanina_city_coordinates:

        # get coordinates from tuple
        lat1, lon1 = (romanina_city_coordinates[city])
        latEnd, lonEnd = (romanina_city_coordinates[end])

        deltaLat = math.radians(latEnd - lat1)
        deltaLon = math.radians(lonEnd - lon1)

       #apply haversine formula
        a = ( (math.sin(deltaLat/2)**2) + math.cos(math.radians(lat1)) * 
             math.cos(math.radians(latEnd)) * (math.sin(deltaLon/2)**2) )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = round(R * c, 2)

        # place city and distance into table
        haversineTable[city] = distance
    # return table of straight line distances
    return haversineTable
