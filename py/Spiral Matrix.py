class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        lret = []
        if matrix == []:
            return []
        
        rows = len(matrix)
        lines = len(matrix[0])
        
        start = 0
        
        while rows - start*2 > 0 and lines - start*2 > 0:
            for i in range(start,lines-start):
                lret.append(matrix[start][i])
                
            for i in range(start+1,rows-start):
                lret.append(matrix[i][lines-start-1])
            
            if rows - start*2 != 1:           ## m != n
                for i in range(start,lines-start-1)[::-1]:
                    lret.append(matrix[rows-start-1][i])
                    
            if lines - start*2 != 1: ## m != n
                for i in range(start+1,rows-start-1)[::-1]:
                    lret.append(matrix[i][start])
                
            start += 1
            
        return lret