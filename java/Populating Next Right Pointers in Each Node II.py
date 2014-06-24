# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def __init__(self):
        self.lnext = []
        
    def traversal(self,root,level):
        if root == None:
            return
        if level == len(self.lnext):
            self.lnext.append([])
            
        self.lnext[level].append(root)
        
        self.traversal(root.left,level+1)
        self.traversal(root.right,level+1)
        
    def connect(self, root):
        self.traversal(root,0)
        
        for l in self.lnext:
            for i in range(len(l)-1):
                l[i].next = l[i+1]