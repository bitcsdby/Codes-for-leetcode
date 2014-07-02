class Solution {
public:
    int reverse(int x) {
        int sign = 1;
        
        if(x < 0)
        {
            sign = -1;
            x = -x;
        }
            
        long long iret = 0;
        
        while(x > 0)
        {
            iret = iret * 10 + x % 10;
            x = x / 10;
        }
        
        return iret * sign;
    }
};