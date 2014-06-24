class Solution:
    # @return a boolean
    def isValid(self, s):
        count = 0;
        small = 0;
        mid = 0;
        big = 0;
        tmp = [];
        
        while count < len(s):
            if s[count] == '(':
                #small = small + 1;
                tmp.append(1);
            elif s[count] == ')':
                #small = small - 1;
                if len(tmp) == 0:
                    return False;
                if tmp.pop() != 1:
                    return False;
                
            elif s[count] == '[':
                #mid = mid + 1;
                tmp.append(2);
            elif s[count] == ']':
                #mid = mid - 1;
                if len(tmp) == 0:
                    return False;
                if tmp.pop() != 2:
                    return False;
                
            elif s[count] == '{':
                #big = big + 1;
                tmp.append(3);
            elif s[count] == '}':
                #big = big - 1;
                if len(tmp) == 0:
                    return False;
                if tmp.pop() != 3:
                    return False;
            count = count + 1;  
                
        if len(tmp) == 0:
            return True;
        else:
            return False;
                
                