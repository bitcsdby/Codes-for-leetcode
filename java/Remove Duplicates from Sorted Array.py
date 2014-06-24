class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0 or len(A) == 1:
            return len(A);
        
        count = 1;
        cur = 1;
        
        while count < len(A):
            if A[count] == A[count - 1]:
                count += 1;
            else:
                A[cur] = A[count];
                cur += 1;
                count += 1;
        
        return cur;