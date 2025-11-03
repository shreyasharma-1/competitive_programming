class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        self.time = 0
        disc = [-1] * n      # discovery time
        low = [-1] * n       # lowest reachable discovery time
        res = []             # store critical edges
        
        def dfs(u, parent):
            self.time += 1
            disc[u] = low[u] = self.time
            
            for v in graph[u]:
                if v == parent:
                    continue
                if disc[v] == -1:  # not visited
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    
                    # if no back edge from v or its subtree to u
                    if low[v] > disc[u]:
                        res.append([u, v])
                else:
                    # back edge
                    low[u] = min(low[u], disc[v])
        
        dfs(0, -1)
        return res
