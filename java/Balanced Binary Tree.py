# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def __init__(self):
        self.ret = True;
    def balance(self,root):
        if root == None:
            return 0;
        left = 0
        right = 0
        
        if root.left != None:
            left = self.balance(root.left) + 1
        if root.right != None:
            right = self.balance(root.right) + 1
        
        dif = left - right;
        if dif < 0:
            dif = -dif;
        if dif > 1:
            self.ret = False;
        return max(left,right)
            
    def isBalanced(self, root):
        self.balance(root)
        return self.ret