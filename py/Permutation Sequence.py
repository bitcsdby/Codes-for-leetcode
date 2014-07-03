class Solution:
    # @return a string
    def first3(self,n,k,lret):
        A99 = 362880
        A88 = 40320
        A77 = 5040
        A66 = 720
        
        if n == 7:
            first = k / A66 + 1
            lret.append(first)
            return k % A66
            
        elif n == 8:
            first = k / A77 + 1
            lret.append(first)
            k = k % A77
            second = k / A66 + 1
            if second >= first:
                second += 1
            lret.append(second)
            return k % A66
            
        elif n == 9:
            first = k / A88 + 1
            k = k % A88
            
            second = k / A77 + 1
            if second >= first:
                second += 1
            k = k % A77
            
            third = k / A66 + 1
            
            add = 0
            for x in range(1,10):
                if x == first:
                    add += 1
                elif x == second:
                    add += 1
                elif x == third + add:
                    break
            third += add
            
            lret.append(first)
            lret.append(second)
            lret.append(third)
            
            return k % A66
            
    def getPermutation(self, n, k):
        lret = []
        sret = ''
        
        if n < 7 or k < 700:
            for i in range(n):
                lret.append(i+1)
        
            for i in range(k-1):
                lret = self.nextPermutation(lret)
        
            sret = ''
        
            for x in lret:
                sret += str(x)
        else:
            lfirst3 = []
            k = self.first3(n,k,lfirst3)
            
            for x in range(n):
                sign = 0
                for i in lfirst3:
                    if x + 1 == i:
                        sign = 1
                        break
                if sign == 0:
                    lret.append(x+1)
            
            for i in range(k-1):
                lret = self.nextPermutation(lret)
            
            sret = ''
            lret = lfirst3 + lret
            
            for x in lret:
                sret += str(x)
                
        return sret
        
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