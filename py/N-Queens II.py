class Solution:
    # @return an integer
    def __init__(self):
        self.iret = 0
        
    def iscut(self,pos,i,j):
        for ipos,x in enumerate(pos):
            if j == x:
                return False
            if abs(ipos - i) == abs(x - j):
                return False
        return True
            
    def nqueen(self,i,n,pos):
        if i == n:
            self.iret += 1
            return
        
        for j in range(n):
            if self.iscut(pos,i,j):
                self.nqueen(i+1,n,pos+[j])
                    
    def totalNQueens(self, n):
        if n == 0:
            return 0
        self.nqueen(0,n,[])
        return self.iret