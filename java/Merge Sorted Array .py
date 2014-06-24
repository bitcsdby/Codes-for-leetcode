class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        counta = 0;
        countb = 0;
        
        if n == 0:
            return;
        elif m == 0:
            while countb < n:
                A.insert(counta,B[countb]);
                m += 1;
                countb += 1;
                counta += 1;
                #print A;
            return;
        
        while counta < m and countb < n:
            if B[countb] < A[counta]:
                A.insert(counta,B[countb]);
                m += 1;
                countb += 1;
            else:
                counta += 1;
            
        while countb < n:
            A.insert(counta,B[countb]);
            m += 1;
            countb += 1;
            counta += 1;
            
        return ;