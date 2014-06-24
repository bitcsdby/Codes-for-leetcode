class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        
        if s == '':
            return False
        
        start = 0
        end = 0
        for c in s:
            if c == ' ':
                start += 1
            else:
                break
        for c in s[::-1]:
            if c == ' ':
                end += 1
            else:
                break
            
        s = s[start:len(s) - end]  ####remove whitespace
        
        signe = 0
        signdot = 0
        signenext = 0  
        
        if s == '':
            return False
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        if s == '':
            return False        ####remove sign
        
        hase = 0
        l = []   
        for c in s:
            if c == 'e':
                l = s.split('e')
                hase = 1
                break
        if hase == 1:
            if l[1] == '' or l[0] == '':
                return False
            if l[1][0] == '+' or l[1][0] == '-':
                l[1] = l[1][1:]
            if l[1] == '':
                return False
            s = 'e'.join(l)     ###remove sign after e
            
        
        for i,c in enumerate(s): ###deal string with no pre or post space,with no extra sign,
            if c == 'e' and signe == 0 :
                if i == 0 or i == len(s) - 1:
                    return False
                signe = 1
                signdot = 1
                continue
            if c == '.' and signdot == 0:
                #num left or right
                
                if i == 0:
                    if i + 1 >= len(s) or s[i+1].isdigit() == False:
                        return False
                elif i != len(s) - 1:
                    if s[i-1].isdigit() == False and s[i+1].isdigit() == False:
                        return False
                else:
                    if s[i-1].isdigit() == False:
                        return False                           
                        
                signdot = 1
                continue
            if c.isdigit() == False:
                return False
        
        return True