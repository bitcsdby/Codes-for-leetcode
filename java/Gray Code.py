class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]
            
        lret = []
        for i in range(2**n):
            lret.append((i>>1)^i)
            
        return lret