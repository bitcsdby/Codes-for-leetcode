class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
            
        lpt = [1,1]
        
        count = 1
        
        while count < rowIndex:
            tmp = [1]
            for i in range(1,count+1):
                tmp.append(lpt[i]+lpt[i-1])
            tmp.append(1)
            lpt = tmp[:]
            count += 1
        
        return lpt