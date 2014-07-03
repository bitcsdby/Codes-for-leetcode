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
        self.bret = True
        
    def isvalid(self,root):
        lret = [root.val]
        
        if root.left != None:
            lleft = self.isvalid(root.left)
            if lleft == []:
                return []
            for x in lleft:
                if root.val <= x:
                    self.bret = False
                    return []
            lret += lleft
                    
        if root.right != None:
            lright = self.isvalid(root.right)
            if lright == []:
                return []
            for x in lright:
                if root.val >= x:
                    self.bret = False
                    return []
            lret += lright
            
        return lret[:]

    def isValidBST(self, root):
        if root == None:
            return True
        self.isvalid(root)
        
        return self.bret 