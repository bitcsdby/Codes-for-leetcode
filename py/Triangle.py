class Solution:
            
    def minimumTotal(self, triangle):
        n = len(triangle)
        min = 0
        matrix = []
        matrix.append([0]*(n+1))
        matrix.append([0]*(n+1))
        
        for i in range(n)[::-1]: #i row
      pre = i + 1
      for j in range(i+1): # j line
          matrix[i%2][j] = (matrix[pre%2][j] if matrix[pre%2][j] < matrix[pre%2][j+1] else matrix[pre%2][j+1]) + triangle[i][j]
        
        return matrix[i%2][0]
            