class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        count = 0;
        
        while count < len(A):
            if A[count] == target or target < A[count]:
                return count;
            count = count + 1;
        
        return count;