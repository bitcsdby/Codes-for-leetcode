class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        total = 0;
        count = 0;
        max = 0;
        
        while count < len(prices) - 1:
            prices[count] = prices[count+1] - prices[count];
            count = count +1;
        
        count = 0;
        
        while count < len(prices) - 1:  #max sub array
            total += prices[count];
            if total > max:
                max = total;
            if total < 0:
                total = 0;
            count = count + 1;
            
        return max;
        
