class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    
    def __init__(self):
        self.lret = []
    
    def perm(self,lcur,sleft):
        lleft = sleft.keys()
        
        zeronum = 0
        for i in sleft.values():
            if i != 0:
                break
            zeronum += 1
            
        if zeronum == len(sleft):
            return self.lret.append(lcur[:])
        
        for x in lleft:
            if sleft[x] != 0:
                lcur.append(x)
            else:
                continue
            sleft[x] -= 1
            self.perm(lcur,sleft)
            lcur.pop()
            sleft[x] += 1
            
        return 
        
            
    def permuteUnique(self, num):
        if len(num) == 1 or len(num) == 0:
            return [num]
        set = {}
        for x in num:
            if set.has_key(x):
                set[x] += 1
            else:
                set[x] = 1
            
        self.perm([],set)
            
        return self.lret;