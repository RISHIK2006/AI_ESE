# Implement Non-Recursive Depth First Search Algorithm. Read the
# undirected unweighted graph from user.

import pandas as pd

# Read edge list from CSV
edges = pd.read_csv("AI_ESE/g.csv", header=None).values  # supports space or tab separation

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
stack = [start_node]
path = []

while stack:
    node = stack.pop()
    if node not in visited:
        visited.add(node)
        path.append(node)
        stack.extend(reversed(graph[node]))


print("\nDFS traversal path:", path)