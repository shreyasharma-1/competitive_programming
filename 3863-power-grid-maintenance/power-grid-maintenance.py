from typing import List
from collections import defaultdict
from sortedcontainers import SortedSet  # pip install sortedcontainers (LeetCode supports it)

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # ---------- Step 1: DSU (Disjoint Set Union) ----------
        parent = [i for i in range(c + 1)]
        rank = [1] * (c + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1

        # ---------- Step 2: Connect all given edges ----------
        for u, v in connections:
            union(u, v)

        # ---------- Step 3: Group stations by their component ----------
        components = defaultdict(list)
        for i in range(1, c + 1):
            components[find(i)].append(i)

        # ---------- Step 4: Track online stations in each component ----------
        component_online = {}
        online = [True] * (c + 1)

        # Initialize each component with all nodes as online (sorted order)
        for root, nodes in components.items():
            component_online[root] = SortedSet(nodes)

        # ---------- Step 5: Process each query ----------
        result = []
        for query in queries:
            t, x = query
            root = find(x)

            if t == 1:
                # Maintenance check query
                if online[x]:
                    result.append(x)
                else:
                    if len(component_online[root]) == 0:
                        result.append(-1)
                    else:
                        result.append(component_online[root][0])

            elif t == 2:
                # Take station offline
                if online[x]:
                    online[x] = False
                    component_online[root].discard(x)

        return result
