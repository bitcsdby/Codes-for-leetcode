class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def swap(self,num,i,j):
        tmp = num[i]
        num[i] = num[j]
        num[j] = tmp
        
    def nextPermutation(self, num):
        if len(num) <= 1:
            return num
        
        i = len(num) - 2
        
        while i >= 0:
            if num[i] < num[i+1]:
                break
            i = i - 1
        
        if i == -1:
            num.reverse()
            return num
        else:
            j = len(num)-1
            while j >= i:
                if num[j] > num[i]:
                    break
                j -= 1
            
            self.swap(num,i,j)
            
            
            tmplist = num[i+1:]
            tmplist.reverse()
            
        return num[:i+1]+tmplist