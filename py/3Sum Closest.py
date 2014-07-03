class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        n = len(num)
        if n == 0:
            return 0
            
        min = 65535 * 65535
        iret = 0
       
        for i in range(n):
            if i != 0 and num[i] == num[i-1]:
                continue
            
            l = i+1
            h = n-1
            
            while l < h:
                if num[l] + num[h] +  num[i] > target:
                    if num[l] + num[h] +  num[i] - target < min:
                        min = num[l] + num[h] +  num[i] - target
                        iret = num[l] + num[h] +  num[i]
                    h -= 1
                elif num[l] + num[h] +  num[i] < target:
                    if target - num[l] - num[h] -  num[i] < min:
                        min = target - (num[l] + num[h] +  num[i])
                        iret = num[l] + num[h] +  num[i]
                    l += 1
                elif num[l] + num[h] +  num[i] == target:
                    iret = num[l] + num[h] +  num[i]
                    return target
                    
        return iret