class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        ls = list(s)
        ls.reverse()
        
        if len(ls) == 0:
            return 0
        
        lrecord = [0]*len(ls)
        
        stack = []
        stackpos = []
        top = -1
        pop = 0
        ipos = 0
        
        while len(ls) != 0:
            tmp = ls.pop()
            if tmp == '(':
                stack.append(tmp)
                top += 1
                stackpos.append(ipos)
            if tmp == ')':
                if top != -1 and stack[top] == '(':
                    stack.pop()
                    pop += 2
                    top -= 1
                    lrecord[top+pop] = 1
                    lrecord[stackpos.pop()] = 1
                else:
                    stack.append(tmp)
                    stackpos.append(ipos)
                    top += 1
            ipos += 1
        
        max = 0
        
        tmpmax = 0
        i = 0
        while i < len(lrecord):  ##record longest consecutive 1 
            if lrecord[i] == 0:
                if tmpmax > max:
                    max = tmpmax
                tmpmax = 0
            elif lrecord[i] == 1:
                tmpmax += 1
                
            i += 1
        if tmpmax > max:
            max = tmpmax
            
        return max