class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        count = 0;
        
        while count < 9:
            c = 0;
            lh = [0] * 9;
            lv = [0] * 9;
            while c < 9:
                if board[count][c] != '.' :
                    if lh[int(board[count][c])-1] == 0:
                        lh[int(board[count][c])-1] = 1;
                    else:
                        return False;
                if board[c][count] != '.':
                    if lv[int(board[c][count])-1] == 0:
                        lv[int(board[c][count])-1] = 1;
                    else:
                        return False;
                c += 1;
            count += 1;
        
        count = 0;    
        while count < 7:
            c = 0;
            while c < 7:
                l = [0] * 9;
                for i in range(3):
                    for j in range(3):
                        if board[count+i][c+j] == '.':
                            continue;
                        if l[int(board[count+i][c+j])-1] == 0:
                            l[int(board[count+i][c+j])-1] = 1;
                        else:
                            return False;
                c+= 3;
            count += 3;
        return True;
