class Solution {
public:
    void insert(const vector<int> S, int start, vector<int> &solution, vector<vector<int>> &solutionset)
    {
        if(start == S.size())
            return ;
        
        for (int i = start;i < S.size();i++)
        {
            if(i != start && S[i] == S[i-1])
                continue;
            solution.push_back(S[i]);
            solutionset.push_back(solution);
            
            insert(S,i+1,solution,solutionset);
            
            solution.pop_back();
        }
    }
    vector<vector<int> > subsetsWithDup(vector<int> &S) {
        vector<vector<int>> vret;
        vector<int> empty;
        
        sort(S.begin(),S.end());
        
        vret.push_back(empty);
        
        insert(S,0,empty,vret);
        
        return vret;
    }
};