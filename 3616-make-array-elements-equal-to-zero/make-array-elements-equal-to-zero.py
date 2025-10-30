from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def simulate(nums, start, direction):
            n = len(nums)
            arr = nums[:]           # make a copy so we don’t destroy the input
            curr = start
            dir = direction         # +1 → right,  −1 → left

            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += dir
                else:
                    arr[curr] -= 1
                    dir *= -1       # reverse direction
                    curr += dir
            return all(x == 0 for x in arr)

        valid = 0
        n = len(nums)

        # Try every position that starts with 0
        for i in range(n):
            if nums[i] == 0:
                if simulate(nums, i, 1):   # → right direction
                    valid += 1
                if simulate(nums, i, -1):  # ← left direction
                    valid += 1

        return valid
