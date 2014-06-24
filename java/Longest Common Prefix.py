class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        
        if strs == []:
            return ''
            
        minlen = 65535*65535
        
        for s in strs:
            if len(s) < minlen:
                minlen = len(s)
        lret = []
        
        for i in range(minlen):
            dict = {}
            for x in strs:
                dict[x[i]] = 1
                if len(dict) != 1:
                    return ''.join(lret)
            
            lret.append(dict.keys()[0])
        return ''.join(lret)