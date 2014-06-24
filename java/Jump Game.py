class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        l = len(A)
        if l == 0:
            return False
        
        max = 0
        for i in range(l):
            if max < i:
                return False
            if max >= l-1:
                break;
            if A[i]+i > max:
                max = A[i]+i
                
        return True