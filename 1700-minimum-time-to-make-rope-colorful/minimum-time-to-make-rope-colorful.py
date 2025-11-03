class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        prev = 0  # index of previous balloon to compare
        
        for i in range(1, len(colors)):
            if colors[i] == colors[prev]:  # same color, remove one
                # Remove the one with smaller time
                total_time += min(neededTime[i], neededTime[prev])
                
                # Keep the one with higher time
                if neededTime[i] > neededTime[prev]:
                    prev = i
            else:
                prev = i
        
        return total_time
