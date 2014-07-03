class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxsubsum(self,arr,dp):
        tmpmax = 0
        max = 0
        
        for i,x in enumerate(arr):
            tmpmax += x
            
            if tmpmax > max:
                max = tmpmax
            if tmpmax < 0:
                tmpmax = 0
            dp[i] = max
            
            
        
    def maxProfit(self, prices):
        
        n = len(prices)
        dif = [0] * n
        
        for i in range(1,n):
            dif[i] = prices[i] - prices[i-1]
            
        dp = [[0]*n]
        dp.append([0]*n)
        
        iret = 0
        
        self.maxsubsum(dif,dp[0])
        dif.reverse()
        
        self.maxsubsum(dif,dp[1])
        dp[1].reverse()
        
        for i in range(n-1):
            if dp[0][i] + dp[1][i+1] > iret:
                iret = dp[0][i] + dp[1][i+1]
                
        return iret