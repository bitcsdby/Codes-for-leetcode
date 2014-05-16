# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        l = [];
        lnode = [];
        
        if root == None:
            return l;

        lnode.append(root);
        
        while len(lnode) != 0:
            tmp = lnode.pop();
            l.append(tmp.val);
            
            if tmp.right != None:
                lnode.append(tmp.right);
            if tmp.left != None:
                lnode.append(tmp.left);
        
        return l;