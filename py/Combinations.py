class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        lret = []
        for i in range(1,n-k+2):
            lret.append([i])
        
        count = 0;
        
        while count < k-1:
            c = 0
            tmp = []
            while c < len(lret):
                for i in range(lret[c][count]+1,n+1):
                    tmp.append(lret[c] + [i]);
                c += 1;
            lret = tmp[:]
            count += 1
            
        return lret;