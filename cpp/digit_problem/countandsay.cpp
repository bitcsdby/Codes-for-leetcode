class Solution {
public:
    string cas(string str)
    {
        string sret = "";
        
        char last = str[0];
        int count = 1;
        
        for(int i = 1;i < str.length();i++)
        {
            if(str[i] == last)
                count += 1;
            else
            {
                sret += ('0'+count);
                sret += last;
                count = 1;
                last = str[i];
            }
        }
        
        sret += ('0'+count);
        sret += last;
        return sret;
    }

    string countAndSay(int n) {
        if(n == 0)
            return "";
        string sret = "1";
        for(int i = 1;i < n;i++)        
            sret = cas(sret);
        
        return sret;
    }   
};