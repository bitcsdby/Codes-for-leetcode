class Solution {
public:
    int sqrt(int x) {
        
        int h = x;
        int l = 0;
        double mid = x;
        double last = 0;
        
        if(x == 0)
            return 0;
        
        while(true)
        {
            last = mid;
            mid = mid / 2.0 + x / 2.0 / mid;
            
            if(abs(mid - last) < 0.01)
                break;
        }
        return (int)mid;
    }
};