class Solution {
public:
    int numDecodings(string s) {
            
        vector<int> dp(s.length(),0);
        if(s.length() == 0)
            return 0;
        
        if(s[0] == '0')    
            return 0;
        if(s.length() <= 1)
            return 1;
        
        dp[0] = 1;
        dp[1] = (s[1] == '0'?0:1) + (atoi(s.substr(0,2).c_str()) <= 26?1:0);
        
        for(int i = 2;i < s.length();i++)
        {
            if(s[i] != '0')
                dp[i] += dp[i-1];
            if((s[i-1] == '1' || s[i-1] == '2') && atoi(s.substr(i-1,2).c_str()) <= 26)
                dp[i] += dp[i-2];
        }
        
        return dp[s.length()-1];
    }
};