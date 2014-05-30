class Solution:
    # @param an integer
    # @return a list of string
    def __init__(self):
        self.lsolution = [];
        self.num = 0;
    def generateParenthesis(self, n):
        self.num = n;
        #slef.lsolution = [''] * n;
        self.parentheses(0,0,['']*2*n);
        return self.lsolution;
        
        
    def parentheses(self,l,r,solution):
        if l == self.num and r == self.num:
            self.lsolution.append(''.join(solution));
            return ;
        if r > l:
            return;
        if l < self.num:
            solution[r+l] = '(';
            self.parentheses(l+1,r,solution);
            
        if r < self.num:
            solution[r+l] = ')';
            self.parentheses(l,r+1,solution);