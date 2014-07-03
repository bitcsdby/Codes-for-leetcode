class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) <= 1:
            return 0
            
        dp = [65535] * len(A)
        dp[0] = 0
        
        for i in range(len(A)):
            if A[i] >= len(A) - i - 1:
                return dp[i] + 1
            for j in range(1,A[i]+1):
                if dp[i] + 1 < dp[j+i]:
                    dp[j+i] = dp[i] + 1
                    if A[j] >= len(A) - j - 1:
                        return dp[j] + 1
        
                
        return dp[len(A)-1]