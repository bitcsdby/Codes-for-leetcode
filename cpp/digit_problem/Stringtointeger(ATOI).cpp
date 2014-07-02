class Solution {
public:
    int atoi(const char *str) {
        int l = 0;
        const char * p = str;
        int sign = 1;
        bool bsign = false,bspace = false;
        long long iret = 0;
        
        while (p != NULL && *p != '\0')
        {
            p++;
            l++;
        }
        
        int i = 0;
        
        for(i = 0;i < l;i++)
        {
            if((str[i] == '+' || str[i] == '-') && bsign == false)
            {
                if(str[i] == '-')
                    sign = -1;
                    
                bsign = true;
                bspace = true;
            }
            else if(str[i] == ' ' && bspace == false)
            {
                continue;
            }
            else if(str[i] >= '0' && str[i] <= '9')
            {
                iret = iret * 10 + str[i] - '0';
                bspace = true;
                bsign = true;
            }
            else
                break;
        }
        
        
        if(iret*sign > INT_MAX)
            return INT_MAX;
        if(iret*sign < INT_MIN)
            return INT_MIN;
            
        return iret*sign;
    }
};