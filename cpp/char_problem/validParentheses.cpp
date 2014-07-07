class Solution {
public:
    bool isValid(string s) {
        int small = 0,mid = 0,big = 0;
        stack<char> st;
        
        for(int i = 0;i < s.length();i++)
        {
            if(s[i] == ')')
            {
                if(st.size() != 0 && st.top() == '(')
                    st.pop();
                else
                    return false;
            }
            else if(s[i] == ']')
            {
                if(st.size() != 0 && st.top() == '[')
                    st.pop();
                else
                    return false;
            }
            else if(s[i] == '}')
            {
                if(st.size() != 0 && st.top() == '{')
                    st.pop();
                else
                    return false;
            }   
            else
                st.push(s[i]);
        }
        
        return st.size() == 0;
        
    }
};