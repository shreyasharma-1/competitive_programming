class Solution:
    def mySqrt(self, x: int) -> int:
        # Edge cases
        if x == 0 or x == 1:
            return x
        
        # Newton’s method function
        def sqt(n):
            x = n
            y = 1
            accuracy = 0.000001  # precision control
            
            while abs(x - y) > accuracy:  # use abs() for positive difference
                x = (x + y) / 2
                y = n / x
            return x
        
        result = sqt(x)
        return int(result)   # return the integer part (floor value)
