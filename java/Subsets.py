class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    
    def subsets(self, S):
        
        l = len(S)
        S.sort()
        lret = []
        
        if l == 0:
            return []
            
        list_binary = [0] * l
        
        size = 1
        
        for i in range(l):
            size *= 2 
            
        count = 0
        while count < size:
            tmp = []
            
            for i in range(l):
                if (count >> i) & 1 == 1:
                    tmp.append(S[i]);
            lret.append(tmp[:])
            count += 1
            
        return lret