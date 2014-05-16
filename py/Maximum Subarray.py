class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if A == None:
            return 0;
            
        count = 0;
        sign = 0;
        maxnag = -65535;
        max = 0;
        add = 0;
        
        while count < len(A):
            if A[count] >= 0:  #存在正数或者0
                sign = 1;
            if A[count] < 0 and A[count] > maxnag: #得到最大负数的值，这个用于全负的情况
                maxnag = A[count];
            
            add += A[count];
            if add < 0:
                add = 0;
            if add > max:
                max = add;
            count = count + 1;
        
        if sign == 1:  #有正数，则返回常规算法最大值
            return max;
        else:
            return maxnag;
        