class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == '':
            return True
        s = s.upper()
        l = 0
        h = len(s)-1
        
        while l <= h:
            #if s[l].isalpha() == False or s[h].isalpha() == False:
            while s[l].isalnum() == False:
                l += 1
                if l >= h:
                    return True
            while s[h].isalnum() == False:
                h -= 1
                if l >= h:
                    return True
                
            if s[l] == s[h]:
                l += 1
                h -= 1
            else:
                return False
            
        return True