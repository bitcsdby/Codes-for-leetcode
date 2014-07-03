class Solution:
    # @return a string
    def join(self,lret):
        ltmp = []
        for x in lret:
            ltmp += x
        return ''.join(ltmp)
        
    def convert(self, s, nRows):
        lret = []
        for i in range(nRows):
            lret.append([])
        
        ls = list(s)
        ls.reverse()
        
        while len(ls) != 0:
            
            for i in range(nRows):
                if len(ls) == 0:
                    return self.join(lret)
                stmp = ls.pop()
                lret[i].append(stmp)
                
            for i in range(nRows-2):
                if len(ls) == 0:
                    return self.join(lret)
                stmp = ls.pop()
                lret[nRows - i - 2].append(stmp)
                
        return self.join(lret)