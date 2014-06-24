class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        rows = len(matrix)
        lines = len(matrix[0])
        
        firstzero = 0
        keyrow = -1
        keyline = -1
        
        for i in range(rows):
            for j in range(lines):
                if firstzero == 0 and matrix[i][j] == 0:
                    keyrow = i
                    keyline = j
                    firstzero = 1
                if matrix[i][j] == 0:
                    matrix[keyrow][j] = 0
                    matrix[i][keyline] = 0
            
        for i in range(rows):
            if i == keyrow:
                continue
            for j in range(lines):
                if j == keyline:
                    continue
                if matrix[keyrow][j] == 0:
                    matrix[i][j] = 0
                    continue        
                if matrix[i][keyline] == 0:
                    matrix[i][j] = 0
        
        if firstzero != 0:
            for i in range(lines):
                matrix[keyrow][i] = 0
            for i in range(rows):
                matrix[i][keyline] = 0