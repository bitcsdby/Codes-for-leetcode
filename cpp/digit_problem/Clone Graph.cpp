/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        map<int ,int> labelmap;
        map<int,UndirectedGraphNode*> nodemap;
        
        
        queue<UndirectedGraphNode*> qgraph;
        
        if(node == NULL)
            return NULL;
        
        qgraph.push(node);
        UndirectedGraphNode *newhead = new UndirectedGraphNode(node->label);
        
        nodemap[node->label] = newhead;
        labelmap[node->label] = 1;
        
        
        while(qgraph.size() != 0)
        {
            UndirectedGraphNode* tmpnode = qgraph.front();
            qgraph.pop();
            
            for(int i = 0;i < tmpnode->neighbors.size();i++)
            {
                if(labelmap.find(tmpnode->neighbors[i]->label) == labelmap.end())
                {
                    labelmap[tmpnode->neighbors[i]->label] = 1;
                    qgraph.push(tmpnode->neighbors[i]);
                }
                
                if(nodemap.find(tmpnode->neighbors[i]->label) == nodemap.end())
                {
                    UndirectedGraphNode* newnode = new UndirectedGraphNode(tmpnode->neighbors[i]->label);
                    nodemap[tmpnode->neighbors[i]->label] = newnode;
                    
                    nodemap[tmpnode->label]->neighbors.push_back(newnode);
                }
                else
                {
                    nodemap[tmpnode->label]->neighbors.push_back(nodemap[tmpnode->neighbors[i]->label]);
                }
            }
        }
        
        return newhead;
    }
};