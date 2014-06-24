class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        #fibbonaqi
        if n == 0 or n == 1 or n == 2:
            return n;
        
        l = [];
        l.append(1);
        l.append(2);
        
        count = 2;
        while count < n:
            l.append(l[count-1]+l[count-2]);
            count += 1;
            
        return l[count-1];
        