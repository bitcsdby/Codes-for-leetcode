class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        tmp = 0;
        for a in A:
            tmp = tmp ^ a; # A xor A = 0  A xor 0 = A
        
        return tmp;