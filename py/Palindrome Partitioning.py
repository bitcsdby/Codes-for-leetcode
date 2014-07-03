class Solution:
    # @param s, a string
    # @return a list of lists of string
    def ispalindrome(self,s):
        ls = len(s) 
        l = 0
        h = 0
        if ls % 2 == 1:
            l = h = ls / 2
        if ls % 2 == 0:
            l = ls / 2 - 1
            h = ls / 2
        while l >= 0 and h < ls and s[l] == s[h]:
            l -= 1
            h += 1
            
        if l == -1:
            return True
        else:
            return False
    
    def partdfs(self,s,lstr):
        if len(s) == 0:
            return [lstr]
        
        ls = len(s)
        lret = []
        
        for i in range(ls):
            if self.ispalindrome(s[0:i+1]):
                lret += self.partdfs(s[i+1:],lstr+[s[0:i+1]])
                
        return lret
        
        
        
    def partition(self, s):
        
        ls = len(s)
        lret = []
        
        if ls == 0:
            return []
      
        lret = self.partdfs(s,[])
        
        return lret