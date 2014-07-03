class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def isvalid(self,board,x,y):
        for i in range(9):
            if i != y and board[x][y] == board[x][i]:
                return False
                
        for i in range(9):
            if i != x and board[x][y] == board[i][y]:
                return False
        
        ix = x / 3 * 3
        jy = y / 3 * 3
        
        for i in range(3):
            for j in range(3):
                if (x != ix+i or y != jy+j) and board[ix+i][jy+j] == board[x][y]:
                    return False
        return True
        
    def solveSudoku(self, board):
        self.solve(board)
    
    def solve(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for x in range(1,10):
                        board[i][j] = str(x)
                        if self.isvalid(board,i,j) == True:
                            if self.solve(board) == True:
                                return True
                        board[i][j] = '.'
                    return False
                    
        return True