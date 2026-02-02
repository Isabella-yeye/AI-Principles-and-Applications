from romaniaDistances import romaina_map

#Implementation of uninformed Depth First Search
def depthFirstSearch(currentCity: str, goalCity: str, path: list[str] = []) -> list[str]:
    """
        Recursive Implementation of DFS

        Args:
            currentCity (string): represents current node visited along 
                path to goal city. 

            goalCity (string): represents desired destination along path

            path (list[str]): list of visited cities, defualts to empty
                list on first run.
        Returns:
            path (list[str]): returns list of visted cities along path
                to goal city

        EX:
            path = depthFirstSearch("Arad", "Rimnicu Vilcea")

    """
    # checl to see if goalCity is in path so it doesnt double up
    if goalCity in path:
        return path
    #check to see of the startCity or currentCity is the goalCity
    elif currentCity == goalCity:
        path.append(currentCity)
        return path
    
    #add city to path list if not already visited and pass on next city
    elif currentCity not in path:
        path.append(currentCity)
        for fringeCity in romaina_map[currentCity]: 
            #traverse fringe cities
            depthFirstSearch(fringeCity[0], goalCity, path)

    return path

# Implementation is unweighted and has bias towards order of fringe cities
# in romaina_map
# version does not check if both cities are in romaina_map keys and will
# return all travelled cities if there is not path to goalCity




            