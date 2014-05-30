class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if A == []:
            return 1
            
        count = 0
        
        while count < len(A):
            if A[count] <= 0 or A[count] == count + 1 or A[count] > len(A) or A[count] == A[A[count]-1]:
                count += 1
            else:
                tmp = A[count]
                A[count] = A[A[count]-1]
                A[tmp-1] = tmp
            
        count = 0

        while count < len(A):
            if count != A[count] - 1:
                break;
            count += 1
        return count+1