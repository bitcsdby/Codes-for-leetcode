class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def __init__(self):
        self.lret = []
    
    def perm(self,lcur,sleft):
        if sleft == {}:
            self.lret.append(lcur[:]);
            return
        
        lleft = sleft.keys()
        
        for x in lleft:
            lcur.append(x)
            del sleft[x]
            self.perm(lcur,sleft)
            lcur.pop()
            sleft[x] = 0
            
        return 
        
            
    def permute(self, num):
        if len(num) == 1 or len(num) == 0:
            return [num]
        set = {}
        for x in num:
            set[x] = 0
            
        self.perm([],set)
            
        return self.lret;