class Solution {
public:
    string simplifyPath(string path) {
        
        vector<string> vs;
        vector<string> st;
        
        for(int i = 0;i < path.length();i++)
        {
            int pos = path.find('/',i);
            string subs = path.substr(i,pos-i);
            vs.push_back(subs);
            i += subs.length();
        }
        
        for(int i = 0;i < vs.size();i++)
        {
            if(vs[i] == "." || vs[i] == "")
                continue;
            else if(vs[i] == "..")
            {
                if(st.size() != 0)
                    st.pop_back();
            }
            else
            {
                st.push_back(vs[i]);
            }
        }
        
        string sret;
        
        for(int i = 0;i < st.size();i++)
        {
            sret += "/";
            sret += st[i];
        }
        
        if(sret == "")
            return "/";
        else
            return sret;
        
    }
};