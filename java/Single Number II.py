class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if len(A) == 1:
            return A[0];
        
        one = 0;
        two = 0;
        three = 0;
        
        for x in A:
            three = two & x;
            two = two | one & x;
            one = one | x;
            
            one = one & ~three;
            two = two & ~three;
            
        return one;
            
        
        
                
        