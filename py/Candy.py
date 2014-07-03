class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        
        i = 1
        l = len(ratings);
        if l <= 1:
            return l;
        lret = [1] * l;
    
        add = 1
        
        while i < l:
            if ratings[i] > ratings[i-1]:
                lret[i] += add 
                add += 1
            else:
                add = 1
            i += 1
            
        i = l-2
        add = 1
        while i >= 0:
            if ratings[i] > ratings[i+1]:
                lret[i] = max(add+1,lret[i]);
                add += 1
            else:
                add = 1
            i -= 1
        
        iret = 0
        for x in lret:
            iret += x;
        
        return iret;