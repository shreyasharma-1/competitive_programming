class Solution:
    def smallestNumber(self, n: int) -> int:
        binary_num = bin(n)[2:]
        x = ""
        for i in binary_num:
            if i == "1":
                x += "1"
            else:
                x += "1"
        res = int(x,2)
        return res
        