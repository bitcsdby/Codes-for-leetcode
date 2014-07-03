class Solution {
public:
    vector<vector<int> > generate(int numRows) {
        vector<vector<int>> vvret;
        vector<int> one(1,1);
        
        if(numRows == 0)
            return vvret;
            
        vvret.push_back(one);
        
        for(int i = 1;i < numRows;i++)
        {
            vector<int> cur;
            
            for(int j = 0;j < i+1;j++)
            {
                if(j == 0)
                    cur.push_back(1);
                else if(j == i)
                    cur.push_back(1);
                else
                {
                    cur.push_back(vvret.back()[j] + vvret.back()[j-1]);
                }
            }
            
            vvret.push_back(cur);
        }
        
        return vvret;
    }
};