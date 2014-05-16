class Solution:
    # @return an integer
    def reverse(self, x):
        ret = 0;
        tmp = 0;
        
        if x < 0:
            x = -x;
            tmp = 1;
        
        
        while x != 0:
            ret = ret * 10 + x % 10;
            x = x / 10;
            
        return ret if tmp == 0 else -ret;