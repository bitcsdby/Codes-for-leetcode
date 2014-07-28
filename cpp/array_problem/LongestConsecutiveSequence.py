class Solution {
public:
    int longestConsecutive(vector<int> &num) {
        unordered_map<int,int> map;
        int iret = 0;
        
        for(int i = 0;i < num.size();i++)
            map[num[i]] = 1;
            
        for(int i = 0;i < num.size();i++)
        {
            if(map[num[i]] == 1)
            {
                int tmplen = 1;
                int left = num[i]-1;
                int right = num[i]+1;
                map[num[i]] = 0;
                
                while(map[left] == 1)
                {
                    map[left] = 0;
                    left -= 1;
                    tmplen += 1;
                }
                
                while(map[right] == 1)
                {
                    map[right] = 0;
                    right += 1;
                    tmplen += 1;
                }
                
                if(tmplen > iret)
                    iret = tmplen;
            }
        }
        
        return iret;
    }
};