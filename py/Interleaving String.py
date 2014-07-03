class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        l1 = len(s1)
        l2 = len(s2)
        
        l3 = len(s3)
        
        if l1+l2 != l3:
            return False
        if l3 == l2 == l1 == 0:
            return True
        
        dp = []
        
        for i in range(l1+1):
            dp.append([False]*(l2+1))
        
        dp[0][0] = True
            
        for i in range(1,l1+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = False
        
        for i in range(1,l2+1):
            if s2[i-1] == s3[i-1]:
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = False
                
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                x = s1[i-1]
                y = s2[j-1]
                z = s3[i+j-1]
                if x == z:
                    dp[i][j] = dp[i-1][j] 
                if y == z:
                    dp[i][j] = dp[i][j-1] or dp[i][j]
                    
        return dp[l1][l2]