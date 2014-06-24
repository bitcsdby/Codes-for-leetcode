class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if m == 0 or n == 0:
            return 0
        if m == 1:
            for x in obstacleGrid[0]:
                if x == 1:
                    return 0
            return 1
        
        grid = []
        for i in range(2):
            grid.append([0]*(n))
            
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            grid[0][i] = 1
            
        if obstacleGrid[1][0] != 1 and obstacleGrid[0][0] != 1:
            grid[1][0] = 1  #scroll array
        
        sign = 0
        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                sign = 1
            if sign == 1:
                grid[i%2][0] = 0
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    grid[i%2][j] = grid[(i-1)%2][j] + grid[i%2][j-1]
                else:
                    grid[i%2][j] = 0
        
        return grid[(m-1)%2][n-1]