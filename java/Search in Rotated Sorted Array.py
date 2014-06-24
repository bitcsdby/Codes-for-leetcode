class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def binarysearch(self,A,target):
        if A == None:
            return -1
        l = 0
        h = len(A) - 1
        
        while l <= h:
            mid = (l+h) / 2
            
            if A[mid] == target:
                return mid
            
            if target > A[mid]:
                l = mid+1
            elif target < A[mid]:
                h = mid-1
        return -1
        
        
    def search(self, A, target):
        if A == None:
            return -1
        
        l = len(A)
        rotate = 0
        while  A[l-1] < A[0]:
            tmp = A.pop()
            A.insert(0,tmp)
            rotate += 1
        
        if rotate != 0:
            lastinA = A[rotate-1]
        else:
            lastinA = A[len(A)-1]
            
        pos = self.binarysearch(A,target)
        
        if pos == -1:
            return -1
        
        if rotate != 0 and target > lastinA:
            return pos - rotate
        elif rotate != 0 and target <= lastinA:
            return len(A)-rotate+pos
        else:
            return pos