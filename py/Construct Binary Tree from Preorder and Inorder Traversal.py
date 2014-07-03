# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def build(self,inorder,preorder):
        if len(preorder) == 0:
            return None
        if len(inorder) == 0:
            return None
            
        iroot = preorder.pop()
        
        root = TreeNode(iroot)
        
        rootindex = inorder.index(iroot)
        
        if rootindex != 0:
            root.left = self.build(inorder[0:rootindex],preorder)
        if rootindex != len(inorder)-1:
            root.right = self.build(inorder[rootindex+1:],preorder)
        
        
        return root
    
    def buildTree(self, preorder, inorder):
        if preorder == []:
            return None
        
        if len(preorder) == 1:
            iroot = preorder.pop()
            root = TreeNode(iroot)
            return root
        preorder.reverse()
            
        iroot = preorder.pop()
        root = TreeNode(iroot)
            
        rootindex = inorder.index(iroot)
        
        if rootindex != 0:
            root.left = self.build(inorder[0:rootindex],preorder)
        if rootindex != len(inorder)-1:
            root.right = self.build(inorder[rootindex+1:],preorder)
        
        
        return root