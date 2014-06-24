class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0:
            return []
        mret = []
        for i in range(n):
            mret += [[0]*n]
        
        count = 0
        num = 1
        
        while count < n:
            
            i = count
            for j in range(count,n-count):
                mret[i][j] = num
                num += 1
            i = n-count-1
            for j in range(count+1,n-count):
                mret[j][i] = num
                num += 1
            for j in range(count,n-count-1)[::-1]:
                mret[i][j] = num
                num += 1
            i = count
            for j in range(count+1,n-count-1)[::-1]:
                mret[j][i] = num
                num += 1
            count += 1
        return mret