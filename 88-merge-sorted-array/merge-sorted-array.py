class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        res = []

        
        for i in range(m):
            res.append(nums1[i])

       
        for i in range(n):
            res.append(nums2[i])

        
        res.sort()

        
        for i in range(m + n):
            nums1[i] = res[i]

        
        for i in range(m + n, len(nums1)):
            nums1[i] = 0
