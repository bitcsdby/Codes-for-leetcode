class Solution:
    # @return a list of lists of string
    def __init__(self):
        self.lret = []
        
    def iscut(self,pos,i,j):
        
        for ipos in range(len(pos)):
            if j == pos[ipos]:
                return False
            if i - ipos == abs(pos[ipos] - j):
                return False
        return True
            
    def nqueen(self,i,n,pos):
        if i == n:
            tmp = []
            for p in range(n):
                tmp.append(['.']*n)
                tmp[p][pos[p]] = 'Q'
            self.lret.append(tmp)
            del pos
            return
        
        for j in range(n):
            if self.iscut(pos,i,j):
                pos.append(j)
                self.nqueen(i+1,n,pos)
                pos.pop()
        del pos
                    
    def solveNQueens(self, n):
        if n == 0:
            return []
        if n == 1:
            return [['Q']]
        self.nqueen(0,n,[])
        
        return self.lret