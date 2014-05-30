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
        self.numlist = [];
    def inorder(self,root):
        
        if root.left == None and root.right == None:  #leaf 
            self.numlist.append(root.val)
            return;
            
        if root.left != None:
            self.inorder(root.left)
        else:
            self.numlist.append(-1);
        
        self.numlist.append(root.val);
        
        if root.right != None:
            self.inorder(root.right)
        else:
            self.numlist.append(-1)
        
        return;
        
    def isSymmetric(self, root):
        if root == None:
            return True;
        if root.left == None and root.right != None:
            return False;
        if root.left != None and root.right == None:
            return False;
        if root.left == None and root.right == None:
            return True;
        if root.left.val != root.right.val:
            return False;
            
        self.inorder(root)
        
        count = 0;
        l = len(self.numlist);
        
        while count < len(self.numlist) / 2:
            if self.numlist[count] != self.numlist[l - count - 1]:
                return False;
            count += 1;
        
        return True;