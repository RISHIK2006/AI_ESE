# Implement A* algorithm. Read undirected weighted graph and heuristic
# values from user.

import heapq
import pandas as pd

print("Enter directed edges in the format src,dst,weight (e.g., 0,1,5). Press Enter on an empty line to finish:")
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
        
    graph[src].append((dst, weight))
    graph[dst].append((src, weight))

# Read heuristic values from CSV
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

# A* algorithm
priority_queue = [(heuristic.get(start_node, float('inf')), 0, start_node)]  # (f, g, node)
came_from = {}  # For path reconstruction
visited = set()

while priority_queue:
    f, g, current = heapq.heappop(priority_queue)

    if current in visited:
        continue

    print(f"f = {g} + {heuristic.get(current, float('inf'))} = {f}")

    visited.add(current)

    if current == goal_node:
        break

    for neighbor, weight in graph.get(current, []):
        if neighbor not in visited:
            new_g = g + weight
            new_f = new_g + heuristic.get(neighbor, float('inf'))
            heapq.heappush(priority_queue, (new_f, new_g, neighbor))
            if neighbor not in came_from or new_g < came_from[neighbor][1]:  # Update only if better g
                came_from[neighbor] = (current, new_g)

# Reconstruct path
path = []
total_cost = 0
node = goal_node

while node != start_node:
    if node not in came_from:
        print("\nNo path found.")
        break
    parent, cost_to_node = came_from[node]
    path.append(node)

    for neighbor, weight in graph[parent]:
        if neighbor == node:
            total_cost += weight  # add the real weight
            break
    node = parent
else:
    path.append(start_node)
    path.reverse()
    print("\nA* Search path:", path)
    print(f"Total path cost: {total_cost}")