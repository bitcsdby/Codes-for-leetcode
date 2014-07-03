class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        
        l1 = len(word1)
        l2 = len(word2)
        
        if l1 == 0:
            return l2
        if l2 == 0:
            return l1
        
        dp = [range(l2+1)]
        
        for i in range(1,l1+1):
            dp.append([i]+[0]*l2)
        
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1, dp[i-1][j-1] + (0 if word1[i-1]==word2[j-1] else 1))
        
        return dp[l1][l2]
