class Solution {
public:
    bool isNumber(const char *s) {
        bool bdot = false,bspace = false,be = false,bsign = false,bnum = false,benum = false;
        
        const char* p = s;
        int l = 0;
        
        while(p != NULL && *p != '\0')
        {
            p += 1;
            l += 1;
        }
        
        int i = 0;
        for(i = 0;i < l;i++)
        {
            if(s[i] == ' ' && bspace == false)
               continue;
            else if(s[i] == ' ' && bspace == true)
            {
                while(i < l && s[i] == ' ')
                   i += 1;
                if(i != l)
                    return false;
                else
                {
                    if(be)  // end with e is not valid
                        return benum;
                }
            }
            else if((s[i] == '+' || s[i] == '-') && bsign == false)
            {
                bsign = true;
                bspace = true;  //no pre space
            }
            else if(s[i] == '.' && bdot == false)
            {
                bdot = true;  // only one bdot
                bsign = true; // sign must before dot
                bspace = true; //space must before dot
            }
            else if(s[i] >= '0' && s[i] <= '9')
            {
                if(be)
                    benum = true;  //num after e
                bnum = true;
                bsign = true;
                bspace = true;
            }
            else if(s[i] == 'e' && be == false && bnum == true)
            {
                be = true;
                bdot = true;
                bsign = false;  //e+10 is valid
            }
            else
            {
                bnum = false;
                break;
            }
           
        }
        if(be)
            return benum && bnum;
        return bnum;
    }
};