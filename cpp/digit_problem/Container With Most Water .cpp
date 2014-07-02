class Solution {
public:
    
    int twomin(int a,int b)
    {
        return a > b ? b : a;
    }
    
    int maxArea(vector<int> &height) {
        int left = 0;
        int right = height.size() - 1;
        int iret = 0;
        
        while(left < right)
        {
            int tmp = twomin(height[left],height[right]);
            
            if(tmp * (right - left) > iret)
            {
                iret = tmp * (right - left);
            }
            
            if(height[left] < height[right])
                left += 1;
            else
                right -= 1;
        }
        
        return iret;
    }
};