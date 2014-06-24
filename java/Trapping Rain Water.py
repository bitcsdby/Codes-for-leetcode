class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self,A):
        l = len(A)
        if l <= 2:
            return 0
        max = 0
        iret = 0
        
        leftmax = [0]*l
        rightmax = [0]*l
        
        for i,x in enumerate(A):
            if x > max:
                max = x
            leftmax[i] = max
        max = 0
        for i,x in enumerate(A[::-1]):
            if x > max:
                max = x
            rightmax[i] = max
        rightmax.reverse()
        
        for i in range(l):
            iret += min(leftmax[i],rightmax[i])-A[i]
        
        return iret