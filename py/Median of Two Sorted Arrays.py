class Solution:
    # @return a float
    def findk(self,A,B,k):
        la = len(A)
        lb = len(B)
        
        if la > lb:
            return self.findk(B,A,k)
            
        if la == 0:
            return B[k-1]
        
        if k <= 1:
            return min(A[0],B[0])
            
        pa = min(k/2,la)
        pb = k-pa
        
        if A[pa-1] < B[pb-1]:
            return self.findk(A[pa:],B,k-pa)
        elif A[pa-1] > B[pb-1]:
            return self.findk(A,B[pb:],k-pb)
        else:
            return A[pa-1]
        
    def findMedianSortedArrays(self, A, B):
        la = len(A)
        lb = len(B)
        
        l = la + lb
        
        if l % 2 == 1:
            return self.findk(A,B,l/2+1)
        if l % 2 == 0:
            return (self.findk(A,B,l/2) + self.findk(A,B,l/2+1)) / 2.0