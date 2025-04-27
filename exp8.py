# Implement A* algorithm. Read directed weighted graph and heuristic
# values from a .csv file.

import heapq
import pandas as pd

edges = pd.read_csv('AI_ESE/gw.csv', header=None).values 

graph = {}
for src, dst, weight in edges:
    src, dst, weight = int(src), int(dst), int(weight)
    if src not in graph:
        graph[src] = []
    graph[src].append((dst, weight))

# Read heuristic values from CSV
heuristics = pd.read_csv('AI_ESE/gh.csv', header=None).values

heuristic = {}
for node, h_value in heuristics:
    node, h_value = int(node), int(h_value)
    heuristic[node] = h_value

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