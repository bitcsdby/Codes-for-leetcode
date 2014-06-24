class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        rows = len(grid)
        lines = len(grid[0])
        
        if rows == 0 or lines == 0:
            return 0
        if rows == 1:
            tmp = 0
            for x in grid[0]:
                tmp += x
            return tmp
        
        dp = []  
        for i in range(2):
            dp.append([0]*lines)
        
        tmp = 0
        for i in range(lines):
            tmp += grid[0][i]
            dp[0][i] = tmp
        
        tmp = grid[0][0]
        for i in range(1,rows):
            tmp += grid[i][0]
            dp[i%2][0] = tmp
            for j in range(1,lines):
                dp[i%2][j] = min(dp[(i-1)%2][j],dp[i%2][j-1]) + grid[i][j]
            
        return dp[(rows-1)%2][lines-1]