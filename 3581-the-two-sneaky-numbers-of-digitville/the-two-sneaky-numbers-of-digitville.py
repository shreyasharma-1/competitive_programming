from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        n = len(nums)
        res = [None, None]
        index = 0
        for i in cnt:
            if cnt[i] == 2:
                if index < len(res):
                    res[index] = i
                    index += 1
        res.sort()
        return res
        