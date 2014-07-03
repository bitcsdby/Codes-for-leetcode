# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def __init__(self):
        self.p1 = None
        self.p2 = None
        self.pre = None
    def inorder(self,root):
        if root == None:
            return 
        
        self.inorder(root.left)
        
        if self.pre != None and self.pre.val > root.val:
            if self.p1 == None:
                self.p1 = self.pre
                self.p2 = root
            else:
                self.p2 = root
                
        self.pre = root
        
        self.inorder(root.right)
        
        
    def recoverTree(self, root):
        
        self.inorder(root)
        
        if self.p1 != None:
            tmp = self.p1.val
            self.p1.val = self.p2.val
            self.p2.val = tmp
            
        return root 