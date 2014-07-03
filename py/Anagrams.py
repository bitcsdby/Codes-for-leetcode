class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def sortstr(self,str):
        l = list(str)
        l.sort()
        return ''.join(l)
        
    def anagrams(self, strs):
        dict = {}
        
        for x in strs:
            stmp = self.sortstr(x)
            if dict.has_key(stmp):
                dict[stmp].append(x)
            else:
                dict[stmp] = [x]
        
        ldict = dict.values()
        lret = []
        for x in ldict:
            if len(x) != 1:
                lret += x
        return lret  #when output limited exceed  appears,check output value and format