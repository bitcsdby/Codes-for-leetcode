class Solution {
public:
    string addBinary(string a, string b) {
        reverse(a.begin(),a.end());
        reverse(b.begin(),b.end());
        
        int lena = a.length();
        int lenb = b.length();
        
        if(lena < lenb)
        {
            string tmp = a;
            a = b;
            b = tmp;
        }
        //a is no shorter than b now
        int c = 0;
        for(int i = 0;i < b.length();i++)
        {
            int tmp = a[i]-'0' + b[i]-'0' + c;
            if(tmp == 3)
            {
                c = 1;
                a[i] = '1';
            }
            else if(tmp == 2)
            {
                c = 1;
                a[i] = '0';
            }
            else if(tmp == 1)
            {
                c = 0;
                a[i] = '1';
            }
            else
            {
                c = 0;
                a[i] = '0';
            }
        }
        
        for(int i = b.length();i < a.length();i++)
        {
            int tmp = a[i]-'0' + c;
            if(tmp == 2)
            {
                c = 1;
                a[i] = '0';
            }
            else if(tmp == 1)
            {
                c = 0;
                a[i] = '1';
                break;
            }
        }
        
        string sret;
        if(c == 1)
        {
            sret = a + "1";
        }
        else
            sret = a;
            
        reverse(sret.begin(),sret.end());
        return sret;
    }
};