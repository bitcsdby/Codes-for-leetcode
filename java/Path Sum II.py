# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def __init__(self):
        self.ll = [];
    def pathSum(self, root, sum):
        if root == None:
            return [];
            
        l = [];
        r = [];
        
        self.ll.append(root.val);
        
        if root.left != None:  
            l = self.pathSum(root.left,sum);
            self.ll.pop();
        if root.right != None:
            r = self.pathSum(root.right,sum);
            self.ll.pop();
            
        
        if root.left == None and root.right == None:
            s = 0;
            tmp = [];
            for x in self.ll:
                s += x;
            if sum == s:
                return [self.ll[:]];
                
        return (l[:] + r[:]);
        