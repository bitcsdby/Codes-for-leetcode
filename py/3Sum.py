class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        n = len(num)
       
        lret = []
       
        for i in range(n):
            
            if num[i] > 0:
                break
            
            if i != 0 and num[i] == num[i-1]:
                continue
            
            l = i+1
            h = n-1
            target = num[i]
            
            while l < h:
                if num[l] + num[h] + target > 0:
                    h -= 1
                    
                elif num[l] + num[h] + target < 0:
                    l += 1
                    
                elif num[l] + num[h] + target == 0:
                    lret.append([target,num[l],num[h]])
                    l += 1
                    h -= 1
                    while l < h and num[l] == num[l-1]:
                        l += 1
                    while l < h and num[h] == num[h+1]:
                        h -= 1
        return lret