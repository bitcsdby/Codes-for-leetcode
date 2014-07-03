class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def __init__(self):
        self.dp = []
    # 1 2 3 4  means last direction is up down left right
    def exi(self,board,i,j,word):
        if word == '':
            return True
        
        up = down = left = right = False
        
        self.dp[i][j] = 1
        
        if i != 0 and self.dp[i-1][j] == 0 and board[i-1][j] == word[0]:
            up = self.exi(board,i-1,j,word[1:]);
            if up == True:
                return True
            
        if i != len(board) - 1 and self.dp[i+1][j] == 0 and board[i+1][j] == word[0]:
            down = self.exi(board,i+1,j,word[1:]);
            if down == True:
                return True
        
        if j != 0 and self.dp[i][j-1] == 0 and board[i][j-1] == word[0]:
            left = self.exi(board,i,j-1,word[1:]);
            if left == True:
                return True
            
        if j != len(board[0]) - 1 and self.dp[i][j+1] == 0 and board[i][j+1] == word[0]:
            right = self.exi(board,i,j+1,word[1:]);
            if right == True:
                return True
                
        self.dp[i][j] = 0 
        return False
        
        
    def exist(self, board, word):
        if board == []:
            return word == '';
        if word == '':
            return True;
            
        rows = len(board);
        lines = len(board[0]);
        
        for i in range(rows):
            for j in range(lines):
                if board[i][j] == word[0]:
                    self.dp = []
                    for x in range(rows):
                        self.dp.append(lines*[0])
                    if self.exi(board,i,j,word[1:]):
                        return True;
        
        return False;