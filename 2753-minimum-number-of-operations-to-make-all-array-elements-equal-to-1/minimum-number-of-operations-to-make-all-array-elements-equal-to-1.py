from math import gcd
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: If the array already contains 1's
        count_ones = nums.count(1)
        if count_ones > 0:
            # We only need to make remaining elements 1
            return n - count_ones

        # Step 2: Find the shortest subarray whose GCD = 1
        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break  # No need to continue further, gcd can't get smaller

        # Step 3: If no subarray with GCD=1 found → impossible
        if min_len == float('inf'):
            return -1

        # Step 4: Total operations
        # - (min_len - 1) operations to make one element = 1
        # - (n - 1) operations to spread 1 to all others
        return (min_len - 1) + (n - 1)

        