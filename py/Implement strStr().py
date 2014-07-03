class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def getnext(self,pattern):
        i = 0
        j = -1
        
        next = [0]*len(pattern)
        next[0] = -1
        
        while i < len(pattern)-1:
            if j == -1 or pattern[i] == pattern[j]:
                i += 1
                j += 1
                if pattern[i] != pattern[j]:
                    next[i] = j
                else:
                    next[i] = next[j]
            else:
                j = next[j]
        return next
                
            
    def strStr(self, haystack, needle):
        i = 0
        j = 0
        if haystack == '' :
            if needle == '':
                return ''
            else:
                return None
        if needle == '':
            return haystack
            
        next = self.getnext(needle)
        
        
        
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
                
        if j == len(needle):
            return haystack[i-len(needle):]
        else:
            return None