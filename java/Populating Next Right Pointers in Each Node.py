# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    def __init__(self):
        self.l = [];
        self.level = 0;
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return;
        self.level += 1;
        self.connect(root.left);
        self.level -= 1;
        
        while len(self.l) <= self.level:
            self.l.append([]);
        self.l[self.level] += [root];
        
        self.level += 1;
        self.connect(root.right);
        self.level -= 1;
        
        if self.level == 0:
            count = 0;
            c = 0;
            
            while count < len(self.l):
                c = 0;
                while c < len(self.l[count]) - 1:
                    self.l[count][c].next = self.l[count][c+1];
                    c += 1;
                if len(self.l[count]) != 0:
                    self.l[count][c].next = None;
                count += 1;
        
        return;