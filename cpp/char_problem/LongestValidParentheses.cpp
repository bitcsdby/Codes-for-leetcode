class Solution {
public:
    int longestValidParentheses(string s) {
        
        if(s.length() == 0)
            return 0;
        
        vector<bool> record(s.length(),false);
        stack<int> pos;
        
        for(int i = 0;i < s.length();i++)
        {
            if(s[i] == '(')
                pos.push(i);
            else if(s[i] == ')')
            {
                if(pos.size() != 0 && s[pos.top()] == '(')
                {
                    record[i] = true;
                    record[pos.top()] = true;
                    pos.pop();
                }
            }
        }
        
        int max = 0;
        int tmpmax = 0;
        for(int i = 0;i < record.size();i++)
        {
            if(record[i] == true)
            {
                tmpmax += 1;
                if(tmpmax > max)
                    max = tmpmax;
            }
            else if(record[i] == false)
            {
                tmpmax = 0;
            }
        }
        
        return max;
    }
};