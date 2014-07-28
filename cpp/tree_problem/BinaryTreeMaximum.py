/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxPathSum(TreeNode *root) {
        int maxpath = -INT_MAX;
        
        traversal(root,maxpath);
        
        return maxpath;
    }
    
    int traversal(TreeNode * root,int &maxpath)
    {
        if(root == NULL)
            return 0;
            
        int l = traversal(root->left,maxpath);
        int r = traversal(root->right,maxpath);
        
        if(maxpath < root->val)
            maxpath = root->val;
        if(maxpath < root->val + l)
            maxpath = root->val + l;
        if(maxpath < root->val + r)
            maxpath = root->val + r;
        if(maxpath < root->val + r + l)
            maxpath = root->val + r + l;
        
        int iret = root->val;
        if(iret < root->val + r)
            iret = root->val+r;
        if(iret < root->val + l)
            iret = root->val+l;
        return iret;
    }

};