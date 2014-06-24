class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if len(gas) == 0:
            return -1;
            
        count = 0;
        while count < len(gas):
            gas[count] = gas[count]-cost[count];     #get a new list, find out sub max sum array and have a test
            count += 1;
            
        count = 0;
        total = 0;
        start = -1;
        max = 0;
        maxstart = 0;
        
        gas += gas;
        
        while count < len(gas):
            if count - start > len(gas)/2:
                break;
            total += gas[count];
            if total < 0:
                start = count + 1;
                total = 0;
            elif start == -1:
                start = count;
            elif total > max:
                max = total;
                maxstart = start;
            count += 1;
        
        count = 0;
        total = 0;
        while count < len(cost):
            total += gas[count + maxstart];
            if total < 0:
                return -1;
            count += 1;
        
        return maxstart;
                
