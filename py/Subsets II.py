class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def __init__(self):
        self.lret = []
        
    def find(self,S,num,lcur):
        if num == len(S):
            #tmp = lcur.sort()
            self.lret.append(lcur[:])
            return
        
        samenum = 1;
        
        while num+samenum < len(S):
            if S[num] == S[num+samenum]:
                samenum += 1
            else:
                break;
                
        for i in range(samenum+1):
            tmp = lcur + [S[num]]*i
            self.find(S,num+samenum,tmp[:])
        
    def subsetsWithDup(self, S):
        if S == None:
            return [[]]
            
        S.sort()
        self.find(S,0,[])
        
        return self.lret