# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root == None:
            return []
            
        lret = []
        
        list_level = []
        list_level.append(root)
        
        while len(list_level) != 0:
            count = 0
            tmp = []
            num = []
            while count < len(list_level):
                if list_level[count].left != None:
                    tmp.append(list_level[count].left)
                if list_level[count].right != None:
                    tmp.append(list_level[count].right)
                num.append(list_level[count].val)
                
                count += 1
                
            lret.append(num[:])
            list_level = tmp[:]
            
        return lret