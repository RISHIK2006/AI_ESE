# 0,1,4
# 0,2,2
# 1,3,5
# 2,3,1
# 2,4,7

# 0,5
# 1,3
# 2,2
# 3,1
# 4,0

# Implement Best First Search Algorithm. Read the undirected weighted
# graph and the heuristic values from user.

import heapq

# Read directed graph from user
print("Enter undirected edges in the format src,dst,weight (e.g., 0,1,5). Press Enter on an empty line to finish:")
graph = {}

while True:
    line = input()
    if not line.strip():
        break

    src_str, dst_str, weight_str = line.split(',')
    src, dst, weight = int(src_str.strip()), int(dst_str.strip()), int(weight_str.strip())
    if src not in graph:
        graph[src] = []
    if dst not in graph:
        graph[dst] = []
        
    graph[src].append((dst, weight))  # save (destination, weight)
    graph[dst].append((src, weight))

# Read heuristic values
print("\nEnter heuristic values in the format node,h(n) (e.g., 0,3). Press Enter on an empty line to finish:")
heuristic = {}

while True:
    line = input()
    if not line.strip():
        break

    node_str, h_str = line.split(',')
    node, h = int(node_str.strip()), int(h_str.strip())
    heuristic[node] = h

start_node = int(input("\nEnter the start node: "))
goal_node = int(input("Enter the goal node: "))

# Best First Search
visited = set()
priority_queue = [(heuristic.get(start_node, 0), start_node)]
path = []

while priority_queue:
    _, current = heapq.heappop(priority_queue)
    if current in visited:
        continue
    visited.add(current)
    path.append(current)

    if current == goal_node:
        break

    for dst, weight in graph.get(current, []):
        if dst not in visited:
            heapq.heappush(priority_queue, (heuristic.get(dst, float('inf')), dst))

print("\nBest First Search path:", path)