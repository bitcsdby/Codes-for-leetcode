class Solution {
public:
    int min(int a,int b)
    {
        return a > b ? b : a;
    }
    int minPathSum(vector<vector<int> > &grid) {
        int rows = grid.size();
        
        if(rows == 0)
            return 0;
            
        int lines = grid[0].size();
        
        if(lines == 0)
            return 0;
        
        vector<vector<int>> map;
        vector<int> line1(lines);
        vector<int> line2(lines);
        
        map.push_back(line1);
        map.push_back(line2);
        
        int rowssum = 0;
        int linessum = 0;
        
        for(int i = 0;i < lines;i++)
        {
            linessum += grid[0][i];
            map[0][i] = linessum;
        }
        
        rowssum = grid[0][0];
        
        for(int i = 1;i < rows;i++)
        {
            rowssum += grid[i][0];
            map[i % 2][0] = rowssum;
            
            for(int j = 1;j < lines;j ++)
            {
                map[i % 2][j] = min(map[(i+1)%2][j],map[i % 2][j-1]) + grid[i][j]; 
            }
        }
        
        return map[(rows-1)%2][lines-1];
        
    }
};