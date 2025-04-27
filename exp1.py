# Implement Recursive Depth First Search Algorithm. Read the undirected
# unweighted graph from a .csv file.

import pandas as pd

# Read edge list from CSV
edges = pd.read_csv("C:/Users\RISHIK\Desktop/AI_ESE/g.csv", header=None).values  # supports space or tab separation

# Build adjacency list
graph = {}
for src, dst in edges:
    src, dst = int(src), int(dst)
    if src not in graph:
        graph[src] = []
    if dst not in graph:
        graph[dst] = []
    graph[src].append(dst)
    graph[dst].append(src)  # since the graph is undirected

# Print graph
print("Graph representation (adjacency list):")
for node, neighbors in graph.items():
    print(f"Node {node} -> {neighbors}")

# DFS
start_node = int(input("Enter the starting node for DFS: "))
visited = set()
path = []

def dfs(node):
    visited.add(node)
    path.append(node)
    print(f"Visiting node {node}")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)

dfs(start_node)
print("\nDFS traversal path:", path)