class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        maxlen = 0
        tmplen = 0
        
        dict = {}
        
        i = 0
        ls = len(s) 
        start = 0
        
        while i < ls:
            if dict.has_key(s[i]):
                if dict[s[i]] < start:
                    dict[s[i]] = i
                    continue
                    
                if tmplen > maxlen:
                    maxlen = tmplen
                tmplen = i-dict[s[i]]
                
                start = dict[s[i]] + 1
                dict[s[i]] = i
            else:
                tmplen += 1
                dict[s[i]] = i
            i += 1
            
        if tmplen > maxlen:
            maxlen = tmplen
            
        return maxlen