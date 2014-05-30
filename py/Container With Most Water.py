# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.mindepth = 65535*65535
    
    def depth(self,root,level):
        if root.left == root.right == None:
            if level < self.mindepth:
                self.mindepth = level;
            return 
        
        if root.left != None:                
            self.depth(root.left,level+1)
        if root.right != None:
            self.depth(root.right,level+1)
        
    def minDepth(self, root):
        if root == None:
            return 0
        self.depth(root,1)
        return self.mindepth