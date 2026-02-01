# Implementation of the Best-First Search algorithm to find a path in a graph using heuristics.
import heapq

def bestFirstSearch(graph, heuristics, start, end):
    # Priority queue to store (heuristic value, current node (city), path taken)
    priorityQueue = [(heuristics[start], start, [start])]
    # Set to keep track of visited nodes
    visited = set()

    # Search while there are nodes to explore
    while priorityQueue:
        # Pop the node with the lowest heuristic value
        _, node, path = heapq.heappop(priorityQueue) # '_' ignores the heuristic value since we don't need it after popping
        
        # If node is the end node (city), return the path
        if node == end:
            return path
        
        # Only expand this node if it hasn't been visited yet
        if node not in visited:
            visited.add(node)
            
            # Explore the neighbors of the current node
            for neighbor, _ in graph[node]:
                # If the neighbor hasn't been visited, add it to the queue
                if neighbor not in visited:
                    # Push the neighbor with its heuristic value and the updated path including the neighbor
                    heapq.heappush(priorityQueue, (heuristics[neighbor], neighbor, path + [neighbor]))