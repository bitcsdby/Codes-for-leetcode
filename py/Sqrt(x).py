class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        small = 0
        big = x
        ret = (small + big) / 2;
        
        if x == 1:
            return 1;
        if x == 0:
            return 0;
        
        while True:
            ret = (small + big) / 2;
            
            if (ret * ret)  <= x and (ret+1)*(ret+1) >= x:
                if ret*ret == x:
                    return ret;
                if (ret+1)*(ret+1) == x:
                    return ret+1;
                return ret;
            if ret * ret < x:
                small = ret + 1;
            if ret * ret > x:
                big = ret - 1;