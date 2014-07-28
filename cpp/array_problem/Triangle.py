class Solution {
public:
    int minimumTotal(vector<vector<int> > &triangle) {
        int l = triangle.size();
        
        if(l == 0)
            return 0;
        if(l == 1)
            return triangle[0][0];
        
        vector<vector<int>> dp;
        vector<int> dp0(l);
        vector<int> dp1(l);
        
        dp.push_back(dp0);
        dp.push_back(dp1);
        
        for(int i = 0;i < l;i++)
            dp[0][i] = triangle[l-1][i];
        
        for(int i = l-1;i > 0;i--)
        {
            for(int j = 0;j < i;j++)
            {
                dp[(l-i) & 0x01][j] = triangle[i-1][j] + (dp[(l-i+1) & 0x01][j] > dp[(l-i+1) & 0x01][j+1]
                                                        ?dp[(l-i+1) & 0x01][j+1]:dp[(l-i+1) & 0x01][j]);
            }
        }
        
        return dp[(l+1) & 0x01][0];
    }
};