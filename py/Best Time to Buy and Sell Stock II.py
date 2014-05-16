class Solution
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices)
        count = 0;
        buy = 0;
        sell = 0;
        total = 0;
        isbought = 0;
        
        while count  len(prices) - 1
            if prices[count+1]  prices[count]
                if isbought == 0
                    buy = prices[count];
                    isbought = 1;
                sell = prices[count+1];
            elif prices[count+1]  prices[count]
                if isbought != 0
                    total += sell - buy;
                    sell = 0;
                    buy = 0;
                    isbought = 0;
            count = count + 1;
        total += sell - buy;
        
        return total;