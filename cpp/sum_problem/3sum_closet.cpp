class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) {
        sort(num.begin(),num.end());
        
        int min = 65536;
        int iret = 0;
        
        for(int i = 0;i < num.size();i++)
        {
            if(i != 0 && num[i] == num[i-1])
                continue;
            
            int p = i+1;
            int j = num.size()-1;
            
            while(p < j)
            {
                int tmp = num[i] + num[j] + num[p];
                
                if(target == tmp)
                {
                    p += 1;
                    j -= 1;
                    while(p < num.size() && num[p] == num[p-1])
                        p += 1;
                    while(j > 0 && num[j] == num[j+1])
                        j -= 1;
                }
                else if(tmp > target)
                {
                    
                    j -= 1;
                }
                else if(tmp < target)
                {
                    p += 1;
                }
                
                if(abs(tmp-target) < min)
                {
                    min = abs(tmp-target);
                    iret = tmp;
                }
            }
        }
        
        return iret;
        
    }
};