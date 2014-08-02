class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {
        
        vector<vector<int>> vret;
        
        if(num.size() == 0)
            return vret;
            
        sort(num.begin(),num.end());
        
        for(int i = 0;i < num.size()-1;i++)
        {
            //remove duplecated results
            if(i > 0 && num[i] == num[i-1]) 
                continue;    
            
            
            int p = i+1;
            int j = num.size() - 1;
        
            while(p < j)
            {
                if(num[p] + num[j] + num[i] == 0)
                {
                    vector<int> tmp;
                    tmp.push_back(num[i]);
                    tmp.push_back(num[p]);
                    tmp.push_back(num[j]);
                    
                    vret.push_back(tmp);
                    p += 1;
                    j -= 1;
                    
                    //remove duplecated results
                    while(p < num.size() && num[p]==num[p - 1]) 
                        p++;    
                    while(j >= 0 && num[j] == num[j + 1]) 
                        j--;
                }
                else if(num[p] + num[j] + num[i] > 0)
                    j -= 1;
                else
                    p += 1;
            }
        }
        
        return vret;
    }
};