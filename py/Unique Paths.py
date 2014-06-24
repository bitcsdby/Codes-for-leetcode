class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        
        if m == 0 or n == 0:
            return 0
        if m == 1:
            return 1
        
        grid = []
        for i in range(2):
            grid.append([0]*(n))
            
        for i in range(n):
            grid[0][i] = 1
        
        grid[1][0] = 1  #scroll array
        
        
        for i in range(1,m):
            for j in range(1,n):
                grid[i%2][j] = grid[(i-1)%2][j] + grid[i%2][j-1]
        
        return grid[(m-1)%2][n-1]