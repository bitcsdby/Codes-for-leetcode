class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        ls = len(S)
        lt = len(T)
        
        if lt == 0:
            return 1
        if lt > ls:
            return 0
        dp = []
        for i in range(ls+1):
            dp.append([1]+[0]*lt)
        
        for i in range(1,ls+1):
            for j in range(1,lt+1):
                dp[i][j] = dp[i-1][j]
                if S[i-1] == T[j-1]:
                    dp[i][j] += dp[i-1][j-1]
                
        return dp[ls][lt]