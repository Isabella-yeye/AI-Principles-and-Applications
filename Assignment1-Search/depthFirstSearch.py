from romaniaDistances import romaina_map

#Implementation of uninformed Depth First Search
def depthFirstSearch(currentCity: str, goalCity: str, path: list[str] = [], metrics = None, depth = 1) -> list[str]:
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
    if path is None:
        path = []

    if metrics is None:
        metrics = {
            "nodes_expanded": 0,
            "max_frontier_size": 0
            }

    metrics["nodes_expanded"] += 1
    metrics["max_frontier_size"] = max(metrics["max_frontier_size"], depth)

    path = path + [currentCity]

    if currentCity == goalCity:
        return {
            "path": path,
            "nodes_expanded": metrics["nodes_expanded"],
            "max_frontier_size": metrics["max_frontier_size"],
            "path_length": len(path) - 1
            }

    for fringeCity in romaina_map[currentCity]:
        if fringeCity[0] not in path:
            result = depthFirstSearch(fringeCity[0], goalCity, path, metrics, depth + 1)
            if result is not None:
                return result

    return None

# Implementation is unweighted and has bias towards order of fringe cities
# in romaina_map
# version does not check if both cities are in romaina_map keys and will
# return all travelled cities if there is not path to goalCity




            