from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda iv: (iv[1], -iv[0]))
        ans = 0
       
        p1 = -10**18
        p2 = -10**18

        for l, r in intervals:
            if l > p2:
               
                p1, p2 = r - 1, r
                ans += 2
            elif l > p1:
              
                p1, p2 = p2, r
                ans += 1
          

        return ans
