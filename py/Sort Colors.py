class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        count = 0;
        
        two = one = zero = -1;
        
        while count < len(A):
            if A[count] == 2:
                two+=1;
                A[two] = 2;
            elif A[count] == 1:
                two+=1;
                one+=1;
                A[two] = 2;
                A[one] = 1;
            elif A[count] == 0:
                two+=1;
                one+=1;
                zero+=1;
                A[two] = 2;
                A[one] = 1;
                A[zero] = 0;
            count += 1;