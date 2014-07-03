# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
   # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root == None:
            return [];
            
        list_thislevel = [];
        list_nextlevel = [];
        
        list_thislevel.append(root);
        
        lret = []
        
        while len(list_thislevel) != 0:
            count = 0;
            tmp = []
            num = []
            while count < len(list_thislevel):
                if list_thislevel[count].left != None:
                    tmp.append(list_thislevel[count].left)
                if list_thislevel[count].right != None:
                    tmp.append(list_thislevel[count].right)
                    
                num.append(list_thislevel[count].val)
                count += 1
            lret.append(num[:])
            list_thislevel = tmp[:];
         
        for i in range(len(lret)):
            if i % 2 == 1:
                lret[i].reverse()
                
        return lret