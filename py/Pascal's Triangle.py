class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return [];
        
        count = 1;
        lret = [];
        
        lret.append([1]);
        
        while count < numRows:
            l = [];
            c = 0;
            l.append(lret[count-1][c]);
            while c < count-1:
                l.append(lret[count-1][c]+lret[count-1][c+1]);
                c += 1;
            l.append(lret[count-1][c]);
            lret.append(l);
            count += 1;
        
        return lret;
            
            
        