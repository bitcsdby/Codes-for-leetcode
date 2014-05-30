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
        self.maxpath = -65535*65535
    def max(self,root):
        if root.val > self.maxpath:
            self.maxpath = root.val
        if root.left == root.right == None:
            return root.val
        
        l = r = 0
        
        if root.left != None:
            l += self.max(root.left)
        if root.right != None:
            r += self.max(root.right)
        
        if max(l+root.val,r+root.val,l+r+root.val) > self.maxpath:
        #if l+r+root.val > self.maxpath:
            self.maxpath = max(l+root.val,r+root.val,l+r+root.val)
            
        #return l+root.val if l > r else r+root.val
        return max(l+root.val,r+root.val,root.val)
        
    def maxPathSum(self, root):
        if root == None:
            return 0
        if root.left == None and root.right ==  None:
            return root.val
            
        self.max(root)
        
        return self.maxpath