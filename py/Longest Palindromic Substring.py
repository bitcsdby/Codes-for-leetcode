class Solution:
    # @return a string
    def getnext(self,pattern):
        i = 0
        j = -1
        next = [0]*len(pattern)
        next[0] = -1
        while i < len(pattern)-1:
            if j == -1 or pattern[i] == pattern[j]:
                j += 1
                i += 1
                
                if pattern[i] != pattern[j]:
                    next[i] = j
                else:
                    next[i] = next[j]
            else:
                j = next[j]
        return next
                
                
    def kmp(self,s,pattern):
        i = 0
        j = 0
        
        next = self.getnext(pattern)
        ls = len(s)
        lp = len(pattern)
        
        max = 0
        
        while i < ls and j < lp:
            if j == -1 or s[i] == pattern[j]:
                j += 1
                i += 1
            else:
                j = next[j]
            if j > max:
                max = j
        
        return max
        
    def longestPalindrome(self, s):
        ls  = list(s)
        ls.reverse()
        sreverse = ''.join(ls)
        
        lens = len(s)
        max = 0
        
        for i in range(lens):
            tmp =  self.kmp(s,sreverse[i:])
            if tmp > max:
                max = tmp
            if len(s) - i < max:
                break
        
        return max