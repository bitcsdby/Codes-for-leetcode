class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def max(self,height):
        stack = []
        
        height.insert(0,0)
        height.append(0)
        
        top = -1
        iret = 0
        
        for i in range(len(height)):
            if top == -1:
                stack.append(i)
                top += 1
            if height[stack[top]] <= height[i]:
                stack.append(i)
                top += 1
            else:
                while top != -1 and height[stack[top]] > height[i]:
                    icur = stack.pop()
                    top -= 1
                    if (i - stack[top] - 1) * height[icur] > iret:
                        iret = (i - stack[top] - 1) * height[icur]
                        
                stack.append(i)
                top += 1
        
        return iret
                
        
    def maximalRectangle(self, matrix):
        dp = []
        if matrix == []:
            return 0
            
        for i in range(len(matrix)):
            dp.append([0]*len(matrix[0]))    
            
        for i in range(len(matrix[0])):
            dp[0][i] = int(matrix[0][i])
            
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j]) == 1:
                    dp[i][j] = dp[i-1][j] + 1
        iret = 0
        
        for i in range(len(matrix)):
            tmp =  self.max(dp[i]) 
            if tmp > iret:
                iret = tmp
        
        return iret