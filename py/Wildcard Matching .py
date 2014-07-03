class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    
    def isMatch(self, s, p):
        
        if p == '*':
            return True
        if s == '':
            return p == ''
        if p == '':
            return False
        
        li = p.split('*')
        ltmp = []
        
        if li[0] == '':
            ltmp.append('')
        for x in li:
            if x != '':
                ltmp.append(x)
                
        if len(''.join(ltmp) ) > len(s):
            return False
            
        if p.endswith('*') and s.startswith(''.join(ltmp)):
            return True
                
        if li[len(li)-1] == '':
            ltmp.append('')
        
        p = '*'.join(ltmp) #remove dupulitcated *
        
        pre = [False]*len(p)
        F = [False]*len(p)
        
        isFirst = 1
        
        for i in range(len(p)):
            if p[i] == '*':
                F[i] = i == 0 or F[i-1]
            elif (p[i] == '?' or p[i] == s[0]) and isFirst == 1:
                isFirst = 0
                F[i] = True
            else:
                break
        
        p += '0'
        
        for x in s[1:]:
            pre = F[:]
            F = [False]*len(p)
            for i in range(len(p)-1):
                if pre[i]:
                    F[i] = F[i] or p[i] == '*'
                    F[i+1] = F[i+1] or p[i+1] == '?' or p[i+1] == x
                elif i == 0 or F[i-1]:
                    F[i] = F[i] or p[i] == '*'
            
        
        return F[len(p)-2]