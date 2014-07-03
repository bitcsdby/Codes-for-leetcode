class Solution {
public:
    vector<int> grayCode(int n) {
        int total = pow(2,n);
        vector<int> vret;
        
        for(int i = 0;i < total;i++)
        {
            vret.push_back((i>>1)^i);
        }
        
        return vret;
    }
};