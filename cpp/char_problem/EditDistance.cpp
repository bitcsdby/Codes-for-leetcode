class Solution {
public:
    int min(int a,int b,int c)
    {
        int iret = a;
        
        if(iret > b)
            iret = b;
        if(iret > c)
            iret = c;
        
        return iret;
    }
    int minDistance(string word1, string word2) {
        int row = word1.length() + 1;
        int line = word2.length() + 1;
        
        vector<int> l(line,0);
        vector<vector<int>> matrix;
        
        for(int i = 0;i < row;i++)
            matrix.push_back(l);
            
        for(int i = 0;i < line;i++)
            matrix[0][i] = i;
            
        for(int i = 0;i < row;i++)
            matrix[i][0] = i;
            
        for(int i = 1;i < row;i++)
            for(int j = 1;j < line;j++)
            {
                matrix[i][j] = min(matrix[i-1][j] + 1,matrix[i][j-1] + 1,matrix[i-1][j-1] + (word1[i-1] == word2[j-1]?0:1));
            }
        
        return matrix[row-1][line-1];
    }
};