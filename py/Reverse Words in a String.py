class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if s == "":
            return ""
            
        lst = s.split(" ")
        lstr = []
        for x in lst:
            if x != '':
                lstr.append(x)
        if len(lstr) == 0:
            return ''
        sret = '';
        
        l = len(lstr);
        count = 0
        while count < l-1:
            tmp = lstr.pop()
            if tmp != '':
                sret += tmp
                sret += ' '
            count += 1
            
        sret += lstr.pop()
        
        return sret;