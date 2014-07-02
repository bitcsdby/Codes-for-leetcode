class Solution {
public:
    int divide(int dividend, int divisor) {
        
        int i = 1;
        int iret = 0;
        int t = 1;
        int sign = 1;
        
        long long newdivisor = (long long)(divisor);
        long long newdividend = (long long)(dividend);

        if(newdivisor == 1)
            return newdividend;
        if(divisor == 2)
            return newdividend >> 1;
        
        if(newdividend > 0 && newdivisor < 0)
        {   
            sign = -1;
            newdivisor = -newdivisor;
        }
        else if(newdividend < 0 && newdivisor > 0)
        {
            sign = -1;
            newdividend = -newdividend;
        }
        else if(newdividend < 0 && newdivisor < 0)
        {
            newdividend = -newdividend;
            newdivisor = -newdivisor;
        }
         
        if(newdividend < newdivisor)
            return 0;
            
        while((newdividend >> i) > (newdivisor << i))
        {
            i += 1;
        }
        
        while(newdividend >= (newdivisor << i))
        {
            newdividend = newdividend - (newdivisor << i);
            iret += 1 << i;
        }
        
        while(newdividend >= newdivisor)
        {
            newdividend = newdividend - newdivisor;
            iret += 1;
        }
        
        if (sign == -1)
            return -iret;
        
        return iret;
    }
};