class Solution {
public:
    int getmax(vector<int> &line)
    {
        stack<int> num;
        num.push(0);
        int iret = 0;
        
        for(int i = 1;i < line.size();i++)
        {
            if(line[i] < line[num.top()])
            {
                while(num.size() != 0 && line[i] < line[num.top()])
                {
                    int cur = num.top();
                    num.pop();
                    
                    if(iret < (i - num.top() - 1) * line[cur])
                        iret = (i - num.top() - 1) * line[cur];
                }
            }
            
            num.push(i);
        }
        
        return iret;
    }
    int maximalRectangle(vector<vector<char> > &matrix) {
        
        if(matrix.size() == 0)
            return 0;
        if(matrix[0].size() == 0)
            return 0;
            
        int iret = 0;
        vector<int> currentline(matrix[0].size()+2,0);
        
        for(int i = 0;i < matrix.size();i++)
        {
            for(int j = 0; j < matrix[i].size();j++)
            {
                if(matrix[i][j] == '0')
                {
                    currentline[j+1] = 0;
                }
                else if(matrix[i][j] == '1')
                {
                    currentline[j+1] += 1;
                }
            }
            
            int tmp = getmax(currentline);
            if(tmp > iret)
                iret = tmp;
        }
        
        return iret;
        
    }
};