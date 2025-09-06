def solve():
    import sys
    from collections import deque, defaultdict
    
    input = sys.stdin.read
    data = input().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        # Build graph
        graph = defaultdict(list)
        edges = []
        
        for i in range(m):
            u = int(data[idx])
            v = int(data[idx + 1])
            idx += 2
            edges.append((u, v))
            graph[u].append((v, i))
            graph[v].append((u, i))
        
        # BFS from node 1 to find shortest distances
        dist_from_1 = [-1] * (n + 1)
        dist_from_1[1] = 0
        queue = deque([1])
        
        while queue:
            node = queue.popleft()
            for neighbor, edge_idx in graph[node]:
                if dist_from_1[neighbor] == -1:
                    dist_from_1[neighbor] = dist_from_1[node] + 1
                    queue.append(neighbor)
        
        # BFS from node n to find shortest distances
        dist_from_n = [-1] * (n + 1)
        dist_from_n[n] = 0
        queue = deque([n])
        
        while queue:
            node = queue.popleft()
            for neighbor, edge_idx in graph[node]:
                if dist_from_n[neighbor] == -1:
                    dist_from_n[neighbor] = dist_from_n[node] + 1
                    queue.append(neighbor)
        
        shortest_path_length = dist_from_1[n]
        
        # Find required edges (bridges in shortest path DAG)
        required_edges = []
        
        for i, (u, v) in enumerate(edges):
            # Check if this edge is on any shortest path from 1 to n
            if (dist_from_1[u] + 1 + dist_from_n[v] == shortest_path_length or
                dist_from_1[v] + 1 + dist_from_n[u] == shortest_path_length):
                
                # Check if this edge is required (bridge)
                # An edge is required if removing it increases shortest path length
                # This happens when it's the only edge connecting two "layers"
                
                # For efficiency, we'll consider an edge required if it's on shortest path
                # and one of its endpoints has exactly one shortest path neighbor in the right direction
                
                min_dist_u = min(dist_from_1[u], dist_from_1[v])
                max_dist_u = max(dist_from_1[u], dist_from_1[v])
                
                if max_dist_u == min_dist_u + 1:  # Edge connects consecutive layers
                    # Count how many shortest path edges lead from layer min_dist to layer max_dist
                    layer_connections = 0
                    for j, (a, b) in enumerate(edges):
                        if ((dist_from_1[a] == min_dist_u and dist_from_1[b] == max_dist_u) or
                            (dist_from_1[b] == min_dist_u and dist_from_1[a] == max_dist_u)):
                            if (dist_from_1[a] + 1 + dist_from_n[b] == shortest_path_length or
                                dist_from_1[b] + 1 + dist_from_n[a] == shortest_path_length):
                                layer_connections += 1
                    
                    if layer_connections == 1:  # This is the only connection between layers
                        required_edges.append(i)
        
        # If no required edges, all answers are -1
        if not required_edges:
            q = int(data[idx])
            idx += 1
            for _ in range(q):
                c = int(data[idx])
                idx += 1
                print(-1)
            continue
        
        # For each query, find closest required edge
        q = int(data[idx])
        idx += 1
        
        for _ in range(q):
            c = int(data[idx])
            idx += 1
            
            min_distance = float('inf')
            closest_edge = -1
            
            for edge_idx in required_edges:
                u, v = edges[edge_idx]
                # Distance from c to this edge
                distance = min(abs(dist_from_1[c] - dist_from_1[u]), 
                             abs(dist_from_1[c] - dist_from_1[v]))
                
                if distance < min_distance or (distance == min_distance and edge_idx < closest_edge):
                    min_distance = distance
                    closest_edge = edge_idx
            
            print(closest_edge + 1)  # Convert to 1-indexed

solve()