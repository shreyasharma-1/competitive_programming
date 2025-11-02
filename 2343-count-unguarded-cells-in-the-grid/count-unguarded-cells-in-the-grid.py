class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        # Mark guards and walls
        for x, y in guards:
            grid[x][y] = 1  # guard
        for x, y in walls:
            grid[x][y] = 2  # wall
        
        # Directions: up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        # Spread vision
        for gx, gy in guards:
            for dx, dy in directions:
                x, y = gx + dx, gy + dy
                while 0 <= x < m and 0 <= y < n and grid[x][y] != 1 and grid[x][y] != 2:
                    if grid[x][y] == 0:
                        grid[x][y] = 3  # mark guarded
                    x += dx
                    y += dy
        
        # Count unguarded (0 = unguarded)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        
        return count
