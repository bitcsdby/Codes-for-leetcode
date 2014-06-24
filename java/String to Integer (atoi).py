class Solution:
    # @return an integer
    def atoi(self, str):
        #l = str.split(' ')
        #str = ''.join(l)     #discard ' '
        end = 0
        sign = 1
        start = 0
        
        for i,c in enumerate(str): # remove non-digit char
            if c != ' ':
                break
            else:
                end += 1
        str = str[end:]  #discard start ' ' 
        
        if str == '':
            return 0
        
        count = 0
        
    #    while count < len(str):
    #        if str[count] == '-':
    #            sign = sign * (-1)
    #            start += 1
    #        elif str[count] == '+':
    #            start += 1
    #        else:
    #            break
    #        count += 1
        if str[0] == '-':
            sign = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        
    #    str = str[start:]  #remove + and -
        
        end = 0
        for i,c in enumerate(str): # remove non-digit char
            if c.isdigit() == False:
                break
            else:
                end += 1
        
        str = str[0:end]
        
        if str == '':
            return 0
            
        ret = 0
        l = list(str)
        #l.reverse()
        
        for c in l:
            ret = ret * 10
            ret += int(c)
        
        if ret > 2147483647 and sign == -1:
            return -2147483648
        
        elif ret > 2147483647:
            return 2147483647 * sign
            
        return ret*sign