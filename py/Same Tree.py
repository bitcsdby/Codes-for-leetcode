# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True;
        elif p == None and q != None:
            return False;
        elif p != None and q == None:
            return False;
        
        l = self.isSameTree(p.left,q.left);
        r = self.isSameTree(p.right,q.right);
        
#        return True if l==True and r==True else False;
        if l == True and r == True:
            return p.val == q.val;
        else:
            return False;
            