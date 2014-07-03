class Solution {
public:
    int largestRectangleArea(vector<int> &height) {
        stack<int> num;
        vector<int>::iterator i = height.begin();
        
        height.insert(i,1,0);
        height.push_back(0);
        
        num.push(0);
        
        int iret = 0;
        
        for(int i = 1;i < height.size();i++)
        {
            if(height[i] < height[num.top()])
            {
                while(num.size() != 0 && height[i] < height[num.top()])
                {
                    int cur = num.top();
                    num.pop();
                    if(iret < (i - num.top() - 1) * height[cur])
                    {
                        iret = (i - num.top() - 1) * height[cur];
                    }
                }
                
            }
            num.push(i);
        }
        
        return iret;
    }
};