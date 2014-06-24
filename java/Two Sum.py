class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        count = 0;
        hashset = {};
        while count < len(num):
            pattern = target - num[count];
            
            if hashset.has_key(pattern): #has pattern
                return (hashset[pattern]+1,count+1);
            if hashset.has_key(num[count]) == False:
                hashset[num[count]] = count;
            count += 1;