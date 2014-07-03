# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generate(self,start,n):
        if n == 0:
            return []
        lret = []
            
        for i in range(n):
            root = TreeNode(i+start)
            rootleft = self.generate(start,i)
            rootright = self.generate(start+i+1,n-i-1)
            
            if rootleft == [] and rootright == []:
                return [root]
            elif rootleft == []:
                for r in rootright:
                    root = TreeNode(i+start)
                    root.right = r
                    lret.append(root)
                continue
            elif rootright == []:
                for l in rootleft:
                    root = TreeNode(i+start)
                    root.left = l
                    lret.append(root)
                continue
            
            for l in rootleft:
                for r in rootright:
                    root = TreeNode(i+start)
                    root.left = l
                    root.right = r
                    lret.append(root)
            
        return lret
        
    def generateTrees(self, n):
        if n == 0:
            return [None]
        lret = []
        root = None
        for i in range(n):
            root = TreeNode(i+1)  #root = i+1
            rootleft = self.generate(1,i)
            rootright = self.generate(i+2,n-i-1)
            
            if rootleft == [] and rootright == []:
                return [root]
            if rootleft == []:
                root.left = None
                for r in rootright:
                    root = TreeNode(i+1)
                    root.right = r
                    lret.append(root)
                continue
            
            if rootright == []:
                root.right = None
                for l in rootleft:
                    root = TreeNode(i+1)
                    root.left = l
                    lret.append(root)
                continue
            
            for l in rootleft:
                for r in rootright:
                    root = TreeNode(i+1)    
                    root.left = l
                    root.right = r
                    lret.append(root)
            
        return lret