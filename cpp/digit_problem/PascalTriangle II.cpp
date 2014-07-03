class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> empty;
        vector<int> last(1,1);
        
        for(int i = 1;i <= rowIndex;i++)
        {
            vector<int> cur;
            
            for(int j = 0;j < i+1;j++)
            {
                if(j == 0)
                    cur.push_back(1);
                else if(j == i)
                    cur.push_back(1);
                else
                {
                    cur.push_back(last[j] + last[j-1]);
                }
            }
            
            last.clear();
            last.insert(last.end(),cur.begin(),cur.end());
        }
        
        return last;
    }
};