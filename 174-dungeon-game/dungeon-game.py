class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Base case: just beyond the princess cell
        dp[m][n - 1] = dp[m - 1][n] = 1

        # Fill DP table backwards
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_health = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, min_health - dungeon[i][j])
        
        return dp[0][0]
