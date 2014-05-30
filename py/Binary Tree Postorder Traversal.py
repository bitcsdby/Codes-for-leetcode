# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root == None:
            return []
            
        lleft = []
        lright = []
        
        lleft = self.postorderTraversal(root.left)
        lright = self.postorderTraversal(root.right)
        lright += [root.val]
        
        
        
        lleft += lright
        
        return lleft[:]