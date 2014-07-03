class Solution {
public:
    double p(double x, int n)
    {
        if(n == 0)
            return 1;
        if(n == 1)
            return x;
        
        double tmp = p(x,n/2);
        
        if(n % 2 == 1)
            return tmp*tmp*x;
        else
            return tmp*tmp;
    }
    double pow(double x, int n) {
        int sign = 1;
        
        if(n == 0)
            return 1;
        
        if(x < 0 && n % 2 == 1)
        {
            x = -x;
            sign = -1;
        }
        
        if(n < 0)
        {
            n = -n;
            return 1/p(x,n) * sign;
        }   
        else
            return p(x,n) * sign;

    }
};