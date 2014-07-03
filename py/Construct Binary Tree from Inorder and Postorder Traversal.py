# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def build(self,inorder,postorder):
        if len(postorder) == 0:
            return None
        if len(inorder) == 0:
            return None
            
        iroot = postorder.pop()
        
        root = TreeNode(iroot)
        
        rootindex = inorder.index(iroot)
        
        if rootindex != len(inorder)-1:
            root.right = self.build(inorder[rootindex+1:],postorder)
        if rootindex != 0:
            root.left = self.build(inorder[0:rootindex],postorder)
        
        return root
    
    def buildTree(self, inorder, postorder):
        if postorder == []:
            return None
        
        if len(postorder) == 1:
            iroot = postorder.pop()
            root = TreeNode(iroot)
            return root
            
        iroot = postorder.pop()
        root = TreeNode(iroot)
        
        
            
        rootindex = inorder.index(iroot)
        
        if rootindex != len(inorder)-1:
            root.right = self.build(inorder[rootindex+1:],postorder)
        if rootindex != 0:
            root.left = self.build(inorder[0:rootindex],postorder)
        
        return root