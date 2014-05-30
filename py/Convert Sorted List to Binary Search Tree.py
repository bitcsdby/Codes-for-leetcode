# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortlist(self,l,start,end):
        if start > end:
            return None
        mid = (start+end)/2
        
        root = TreeNode(l[mid])
        
        root.left = self.sortlist(l,start,mid-1)
        root.right = self.sortlist(l,mid+1,end)
        
        return root
    
    def sortedListToBST(self, head):
        l = []
        
        p = head
        
        while p != None:
            l.append(p.val)
            p = p.next
        
        return self.sortlist(l,0,len(l)-1)