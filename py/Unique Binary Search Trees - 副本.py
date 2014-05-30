class Solution:
    # @return an integer
    def numTrees(self, n):
        
        if n == 0 or n == 1:
            return 1;
            
        l = [];
        l.append(1);
        l.append(1);
        
        count = 2;
        
        while count <= n:
            c = 0;
            tmp = 0;
            while c < count:
                tmp += l[count-c-1] * l[c];
                c += 1;
            l.append(tmp);
            count += 1;
            
        return l.pop();