# Implement Breadth First Search Algorithm. Read the undirected
# unweighted graph from user.

from collections import deque

# Read edge list from user input
print("Enter edges in the format src,dst (e.g., 0,1). Press Enter on an empty line to finish:")
graph = {}

while True:
    line = input()
    if not line.strip():
        break
    
    src_str, dst_str = line.split(',')
    src, dst = int(src_str.strip()), int(dst_str.strip())
    if src not in graph:
        graph[src] = []
    if dst not in graph:
        graph[dst] = []
    graph[src].append(dst)
    graph[dst].append(src)  # undirected

# Print graph
print("\nGraph representation (adjacency list):")
for node, neighbors in graph.items():
    print(f"Node {node} -> {neighbors}")

# BFS
start_node = int(input("\nEnter the starting node for BFS: "))
visited = set()
queue = deque([start_node])
path = []

while queue:
    node = queue.popleft()
    if node not in visited:
        visited.add(node)
        path.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

print("\nBFS traversal path:", path)