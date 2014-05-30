class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 2:
            return len(A);
        
        count = 1;
        cur = 1;
        sign = 0;
        
        while count < len(A):
            if A[count] == A[count - 1]:
                if sign == 0:
                    A[cur] = A[count]
                    sign += 1;
                    cur += 1;
                count += 1;
            else:
                sign = 0
                A[cur] = A[count];
                cur += 1;
                count += 1;
            
            
        return cur;