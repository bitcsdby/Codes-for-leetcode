class Solution:
    # @param s, a string
    # @return a list of strings
    def restore(self,s,lip):
        ldomin = len(lip)
        lret = []
        
        if len(s) < 4-ldomin or len(s) > (4 - ldomin) * 3:#valid
            return []
        
        if len(s) == 0: #valid
            return [lip]
            
        str = ''
        str += s[0]
        lret += self.restore(s[1:],lip+[str])
        
        if s[0] == '0':
            return lret
        
        if len(s) > 1:
            str += s[1]
            lret += self.restore(s[2:],lip+[str])
            
        if len(s) > 2 and int(s[0]) <= 2:
            str += s[2]
            if int(str) <= 255:
                lret += self.restore(s[3:],lip+[str])
            
        return lret
        
    def restoreIpAddresses(self, s):
        lret = []
        lret = self.restore(s,[])
        sret = []
        
        for x in lret:
            sret.append('.'.join(x))
            
        return sret