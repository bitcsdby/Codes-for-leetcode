class Solution {
public:
    int f(int n)
    {
        if(n == 1)
            return 1;
            
        return n*f(n-1);
    }
    vector<vector<int> > permute(vector<int> &num) {
        
        vector<vector<int>> ret;
        
        if(num.size() == 0)
            return ret;
        
        int total = f(num.size());
        
        ret.push_back(num);
        
        for(int i = 1;i < total;i++)
        {
            next_permutation(num.begin(),num.end());
            ret.push_back(num);
        }
        
        return ret;
        
    }
};