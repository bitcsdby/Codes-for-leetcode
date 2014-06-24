class Solution:
    # @param path, a string
    # @return a string
    
    def simplifyPath(self, path):
        
        lpath = path.split('/')
        stack_path = []
        lret = []
        
        sign = 0
        for tmpstr in lpath:
            if tmpstr == '':
                continue
            if tmpstr == '.':
                continue
            if tmpstr == '..':
                if len(stack_path) != 0:
                    stack_path.pop()
                continue
            stack_path.append(tmpstr)
        
        
        if len(stack_path) == 0:
            return '/'
        
        for x in stack_path:
            lret.append('/')
            lret.append(x)
        
        return ''.join(lret)