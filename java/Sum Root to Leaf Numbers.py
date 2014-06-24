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
        self.sum = 0
        self.strnum = []
    
    def sumnum(self,root):
        self.strnum.append(str(root.val))
       
        if root.left == root.right == None:
            self.sum += int(''.join(self.strnum))
            self.strnum.pop()
            return 
        
        if root.left != None:
            self.sumnum(root.left)
            
        if root.right != None:
            self.sumnum(root.right)
        
        self.strnum.pop()
        
            
    def sumNumbers(self, root):
        if root == None:
            return 0
        self.sumnum(root)
        return self.sum