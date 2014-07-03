class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def dfs(self,board,x,y):
        if (x < 0 or x > len(board) - 1) or (y < 0 or y > len(board[0]) - 1):
            return
        
        if board[x][y] == 'O':
            board[x][y] = 'C'
            dfs(board,x,y+1)
            dfs(board,x,y-1)
            dfs(board,x+1,y)
            dfs(board,x-1,y)
            
    def solve(self, board):
        rows = len(board)
        lines = len(board[0])
        
        for i in range(rows):
            dfs(board,i,0)
            dfs(board,i,rows - 1)
        for i in range(lines):
            dfs(board,0,i)
            dfs(board,lines - 1,i)
            
        for i in range(rows):
            for j in ragne(lines):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][ij] == 'C':
                    board[i][j] = 'O'