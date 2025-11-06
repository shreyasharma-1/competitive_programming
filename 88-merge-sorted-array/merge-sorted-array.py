class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Collect the first m elements from nums1 (including zeros that are valid values)
        res = []
        for i in range(m):
            res.append(nums1[i])

        # Collect the first n elements from nums2
        for i in range(n):
            res.append(nums2[i])

        
        res.sort()

        
        for i in range(m + n):
            nums1[i] = res[i]

        # If nums1 is larger than m+n, fill remaining slots with zeros (optional but safe)
        for i in range(m + n, len(nums1)):
            nums1[i] = 0
