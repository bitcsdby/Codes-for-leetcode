class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0 / self.pow(x,-n)
        
        half = pow(x,n>>1)
        
        if n % 2 == 0:
            return half*half
        else:
            return half*half*x