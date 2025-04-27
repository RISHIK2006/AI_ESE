# Implement Best First Search Algorithm. Read the directed weighted graph
# and the heuristic values from user.

import heapq

print("Enter directed egdes with weights in src,dst,wt format: ")
graph = {}

while True:
    line = input()
    if not line.strip():
        break;
    
    src_str, dst_str, wt_str = line.split(',')
    src, dst, wt = int(src_str.strip()), int(dst_str.strip()), int(wt_str.strip())
    
    if src not in graph:
        graph[src] = []
        
    graph[src].append((dst, wt))
    

print("Enter heuristic value of each node in node,h(n) format: ")
heuristic = {}

while True:
    line = input()
    if not line.strip():
        break;
    
    node_str, h_str = line.split(',')
    node, h = int(node_str.strip()), int(h_str.strip()) 
    heuristic[node].append(h);
    
start_node = int(input("\nEnter the start node: "))
goal_node = int(input("Enter the goal node: "))

visited = set()
path = []
pq = [(heuristic.get(start_node, 0), start_node)]

while pq:
    _, current = heapq.heappop(pq)
    
    if current in visited:
        continue
    
    visited.add(current)
    path.append(current)
    
    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            heapq.heappush(pq, (heuristic.get(neighbor, float('inf')), neighbor))
            
print("\nBest First Search path:", path)
