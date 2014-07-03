# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        
        if node == None:
            return None;
        
        head = UndirectedGraphNode(node.label);
        dict = {head.label:head}
        
        queue = []
            
        queue.insert(0,node)
        
        while queue != []:
            tmpnode = queue.pop();
            
            for x in tmpnode.neighbors:
                if dict.has_key(x.label) == False:
                    p = UndirectedGraphNode(x.label);
                    queue.insert(0,x);
                    dict[x.label] = p;
                    dict[tmpnode.label].neighbors.append(p);
                else:
                    dict[tmpnode.label].neighbors.append(dict[x.label]);
        
        return head