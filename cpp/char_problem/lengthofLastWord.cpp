class Solution {
public:
    int lengthOfLastWord(const char *s) {
        
        int len = 0;
        const char* p = s;
        
        while(p != NULL && *p != '\0')
        {
            p += 1;
            len += 1;
        }
        
        if(len == 0)
            return 0;
            
        int iret = 0;
        
        for(int i = len-1;i >= 0;i--)
        {
            if(s[i] == ' ')
                continue;
            else
            {
                while(i >= 0 && s[i] != ' ')
                {
                    iret += 1;
                    i -= 1;
                }
                break;
            }
        }
        
        return iret;
    }
};