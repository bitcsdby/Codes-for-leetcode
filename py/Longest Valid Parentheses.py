class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        
        ls = list(s)
        
        ls.reverse()
        
        stack = []
        top = 0
        iret = 0
        maxlenth = 0
        
        while len(ls) != 0:
            stmp = ls.pop()
            if stmp == '(':
                stack.append(stmp)
                top += 1
            if stmp == ')':
                if stack[top-1] == '(':
                    stack.pop()
                    iret += 2
                    top -= 1
            if top == 0:
                    if iret > maxlenth:
                        maxlenth = iret
                        iret = 0
        
        return maxlenth