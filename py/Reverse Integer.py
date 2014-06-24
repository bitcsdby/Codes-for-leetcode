class Solution:
    # @return an integer
    def reverse(self, x):
        sign = 0
        if x < 0:
            sign = 1
            x = -x
        
        l = list(str(x))
        l.reverse()
        ret = int(''.join(l))
        
        if sign == 1:
            return -ret
        return ret