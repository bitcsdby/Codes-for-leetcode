# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        l = [];
        lnode = [];
        
        if root == None:
            return l;
        tmp = root;
        lnode.append(tmp);
        
        while len(lnode) != 0:
            while tmp.left != None and tmp.left.val != -65535:
                lnode.append(tmp.left);
                tmp = tmp.left;
            else:
                tmp = lnode.pop();
                l.append(tmp.val);
                if tmp.right != None:
                    lnode.append(tmp.right);
                tmp.val = -65535;
                if len(lnode) != 0:
                    tmp = lnode[len(lnode)-1];
        return l;