#Implementation of A* bfs
import heapq

# implementation derived from bestFirstSearch implementation
def aStarSearch(graph, heuristics, start, end):
    # Priority queue to store (heuristic value, cost of path (0 for start), current node (city), path taken)
    priorityQueue = [(heuristics[start], 0, start, [start])]
    # Set to keep track of visited nodes
    visited = set()

    # Metric tracking
    nodesExpanded = 0
    maxFrontierSize = len(priorityQueue)

    # Search while there are nodes to explore
    while priorityQueue:
        # Updaet maximum frontier size
        maxFrontierSize = max(maxFrontierSize, len(priorityQueue))

        # Pop the node with the lowest heuristic value
        _, pathCost, node, path = heapq.heappop(priorityQueue) # '_' ignores the heuristic value since we don't need it after popping
        
        # If node is the end node (city), return the path
        if node == end:
            return {
                "path": path,
                "nodes_expanded": nodesExpanded,
                "max_frontier_size": maxFrontierSize,
                "path_length": len(path) - 1
            }
        
        # Only expand this node if it hasn't been visited yet
        if node not in visited:
            visited.add(node)
            nodesExpanded += 1 # Increment for each node expanded
            
            # Explore the neighbors of the current node
            for neighbor, cost in graph[node]:
                # If the neighbor hasn't been visited, add it to the queue
                if neighbor not in visited:
                    #update cost of path (newPathCost) for this each node
                    newPathCost = pathCost + cost
                    # Push the neighbor with its sum of heuristic value and cost, new path cost, and the updated path including the neighbor
                    heapq.heappush(priorityQueue, (heuristics[neighbor] + newPathCost, newPathCost, neighbor, path + [neighbor]))
