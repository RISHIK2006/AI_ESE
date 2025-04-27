# Implement Best First Search Algorithm. Read the undirected unweighted
# graph and the heuristic values from user.

import heapq

print("Enter undirected edges in the format src,dst (e.g., 0,1). Press Enter on an empty line to finish:")
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
    graph[dst].append(src)



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

# Get start and goal
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

    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            heapq.heappush(priority_queue, (heuristic.get(neighbor, float('inf')), neighbor))

print("\nBest First Search path:", path)