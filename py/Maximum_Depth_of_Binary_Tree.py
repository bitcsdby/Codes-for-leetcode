# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0;
        l = self.maxDepth(root.left) + 1;
        r = self.maxDepth(root.right) + 1;
            
        return l if l > r else r;
