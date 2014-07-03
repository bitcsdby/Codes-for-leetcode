class Solution:
    # @return a boolean
    def __init__(self):
        self.dp = []
    
    def isScra(self,s1,s2):
        if s1 == s2:
            return True
        if len(s2) == 1:
            return s1 == s2
        if len(s2) == 2:
            l1 = list(s1)
            l2 = list(s2)
            l1.sort()
            l2.sort()
            return l1 == l2 
        
        
        ls1 = len(s1)
        ls2 = len(s2)
        
       
        for i in range(1,len(x)):
            ll = list(s2[0:i])
            lr = list(s2[i:])
            
            ll.sort()
            lr.sort()
            
            l0i = s1[0:i]
            l0i2 = s1[len(s1)-i:]
            rin = s1[i:]
            rin2 = s1[0:len(s1)-i]
            
            l0i.sort()
            l0i2.sort()
            rin.sort()
            rin2.sort()
            
            if ll == list(s1[0:i]) and lr = list(s1[i:]): ## left right seprate
            
            
            ileft = self.isScra(s1[0:i],s2[0:i])
            if ileft == False:
                continue
            iright = self.isScra(s1[i:],s2[i:])
            if ileft and iright:
                return True
        
        return False
        
    
    def isScramble(self, s1, s2):
        if len(s2) == 0:
            return s1 == ''
        
        l1 = list(s1)
        l2 = list(s2)
        l1.sort()
        l2.sort()
        if l1 != l2:
            return False
            
        self.dp = [0]*len(s2)
        
        return self.isScra(s1,s2)