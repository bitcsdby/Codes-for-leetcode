class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        n = len(num)
        
        sign = 0
        
        lret = []
        for j in range(n):
            if j != 0 and num[j-1] == num[j]:
                continue
            for i in range(j+1,n):
                if i != j+1 and num[i] == num[i-1]:
                    continue
                
                if num[i]+num[j] > target and num[i] > 0: #use attribution of increasing array 
                    break
                
                l = i+1
                h = n-1
                
                while l < h:
                    sum = num[l] + num[h] + num[i] + num[j]
                    if sum > target:
                        h -= 1
                    elif sum < target:
                        if num[h] > 0 and target - (sum-num[l]) > (num[h] << 1): #consider nagtive
                            break
                        l += 1
                    elif sum == target:
                        lret.append([num[j],num[i],num[l],num[h]])
                        l += 1
                        h -= 1
                        while l < h and num[l] == num[l-1]:
                            l += 1
                        while l < h and num[h] == num[h+1]:
                            h -= 1
        return lret