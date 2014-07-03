class Solution:
    # @param s, a string
    # @return an integer
    # DFS
        
    def numDecodings(self, s):
        
        if s == '':
            return 0
        if len(s) == 1:
            if s == '0':
                return 0
            else:
                return 1
        if s[0] == '0':
            return 0
            
        dp = [0] * len(s)
        
        dp[0] = 1 if s[0] != '0' else 0
        dp[1] = (dp[0] if s[1] != '0' else 0) + (1 if s[0] != '0' and int(s[0:2]) <= 26 else 0)
        
        for i in range(2,len(s)):
            if s[i] != '0':
                dp[i] += dp[i-1]
                
            if (int(s[i-1:i]) == 1 or int(s[i-1:i]) == 2) and int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]
                
        return dp[len(s)-1]