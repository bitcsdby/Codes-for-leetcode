# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def __init__(self):
        self.l = []
    
    def Inorder(self,root):
        if root != None:
            self.l.append(root);
        else:
            return;
        
        self.Inorder(root.left)
        self.Inorder(root.right)
    
    def flatten(self, root):
        if root == None:
            return ;
        
        self.Inorder(root)
        
        n = len(self.l)
        
        for i in range(n-1):
            self.l[i].left = None;
            self.l[i].right = self.l[i+1]
            
        self.l[n-1].left = None
        self.l[n-1].right = None