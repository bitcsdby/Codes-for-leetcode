class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        h = len(matrix)
        v = len(matrix[0])
        
        counth = 0
        
        while counth < h:
            if target == matrix[counth][0]:
                return True
            if target > matrix[counth][0]:
                counth += 1;
            else:
                break;
                
        counth -= 1;
        
        for i in range(v):
            if matrix[counth][i] == target:
                return True
        
        return False