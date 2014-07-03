class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        lret = []
        
        if len(L) == 0:
            return []
            
        litem = len(L[0])
        N = len(L) * litem
        dict = {}
        for i in range(len(L)):
            dict[L[i]] = 1
        
        for i in range(len(S) - N + 2):
            if dict.has_key(S[i:i+litem]) == False:
                continue
            
            for j in range(len(L)):
                dict[L[j]] = 1
            j = 0
            
            while j < len(L):
                stmp = S[i+litem*j : i+litem*j+litem]
                if dict.has_key(stmp) == False or dict[stmp] == 0:
                    break
                dict[stmp] = 0
                j += 1
                
            if j == len(L):
                lret.append(i)
        
        return lret