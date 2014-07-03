class Solution:
    # @return a string
    def say(self,s):
        sret = ''
        i = 0
        scur = ''
        
        while i < len(s):
            count = 1
            scur = s[i]
            i += 1
            while i < len(s) and s[i] == scur:
                count += 1
                i += 1
            sret += str(count)
            sret += scur
            
        return sret[:]
        
    def countAndSay(self, n):
        if n == 0:
            return ''
        if n == 1:
            return '1'
            
        count = 1
        s = '1'
        
        while count < n:
            s =  self.say(s)
            count += 1
            
        return s[:]