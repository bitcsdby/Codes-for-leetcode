class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def subsetcut(self,s,dict,nodict):
        if len(s) == 0:
            return True
        
        l = len(s)
        
        for i in range(l):
            prefix = s[0:i+1]
            if prefix in dict:
                suffix = s[i+1:]
                if suffix in nodict:
                    continue
                if self.subsetcut(suffix,dict,nodict):
                    return True
                else:
                    nodict.add(suffix)
        return False
                
        
    def wordBreak(self, s, dict):
        
        l = len(s)
        nodict = set([])
        
        return self.subsetcut(s,dict,nodict)