class Solution:
    # @return a boolean
    def isMatch(self,s,p):
        l = list(p)
        ltmp = l[:]
        
        i = 0
        while i < len(ltmp):
            if ltmp[i] == '*':
                break
            i += 1
        
        if i != len(ltmp):
            str = ''.join([ltmp[i-1],ltmp[i]])
            tmpp = p[:]
        
            tmpp = tmpp[i+1:]
        
            while tmpp.startswith(str):
                tmpp = tmpp[2:]
            
            return self.ismatch(s,p[:i+1]+tmpp)
        else:
            return self.ismatch(s,p)
            
    def ismatch(self, s, p):
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1:
            return (len(s) == 1) and (p[0] == '.' or p[0] == s[0])
        
        if p[1] == '*':
            j = 0
            while len(s) != j and (s[j] == p[0] or p[0] == '.'):
                if self.isMatch(s[j:],p[2:]):
                    return True
                j += 1
            return self.isMatch(s[j:],p[2:])
                
        else:
            if len(s) != 0 and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:],p[1:])
            
        return False