class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchleft(self,l,h,target,A):
        pcur = h
        while l <= h:
            mid = (l+h)/2
            if A[mid] == target:
                if mid == 0:
                    return 0
                if mid == pcur:
                    return pcur
                if A[mid-1] != target:
                    return mid
                h = mid - 1
            elif A[mid] != target:
                l = mid+1
                
    def searchright(self,l,h,target,A):
        pcur = l
        while l <= h:
            mid = (l+h)/2
            if A[mid] == target:
                if mid == len(A) - 1:
                    return len(A) - 1
                if A[mid+1]  != target:
                    return mid
                l = mid + 1
            elif A[mid] != target:
                h = mid-1
        return pcur-1
    
        
    def searchRange(self, A, target):
        l = 0
        h = len(A)-1
        left = -1
        right = -1
        
        while l <= h:
            mid = (l+h) / 2
            if target > A[mid]:
                l = mid+1
            elif target < A[mid]:
                h = mid-1
            if A[mid] == target:
                left = self.searchleft(0,mid,target,A)
                right = self.searchright(mid+1,len(A)-1,target,A)
                break
            
        return [left,right]