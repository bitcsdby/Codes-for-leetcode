# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean

    def hasPathSum(self, root, sum):
        if root == None:
            return False;
        l = False;
        r = False;
        
        if root.left != None:  
            l = self.hasPathSum(root.left,sum-root.val);
        if root.right != None:
            r = self.hasPathSum(root.right,sum-root.val);
            
        if root.left == None and root.right == None:
            if sum - root.val == 0:
                return True;
                
        if l == True or r == True:
            return True;
        else:
            return False;