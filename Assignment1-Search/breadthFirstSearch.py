# Implementation for breadth first search (BFS) algorithm
from collections import deque

# Recieves a graph represented as an adjacency list, a start node, and an end node
def breadthFirstSearch(graph, start, end):
    # Intialize the queue with a path that starts at the start node
    queue = deque([[start]])
    visited = set() # Set to keep track of visited nodes

    # Search while there are paths to explore
    while queue:
        path = queue.popleft() # Remove the leftmost path from the queue (First In First Out - FIFO)
        node = path[-1] # Current node is the last node in the path

        # If node is the end node, return the path
        if node == end:
            return path

        # Only expand this node if it hasn't been visited yet
        if node not in visited:
            visited.add(node)

            # Look at the neighbors of the current node
            for neighbor, _ in graph[node]:
                new_path = list(path) # Create a new path extending the current path
                new_path.append(neighbor)
                queue.append(new_path) # Add the new path to the queue