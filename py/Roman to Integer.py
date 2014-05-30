class Solution:
    # @return an integer
    
    def __init__(self):
        self.count = 0;
    def getInteger(self,a,b,c,s):
        if self.count < len(s) and  s[self.count] == a: #1 2 3 4 and 9
            if self.count+1 < len(s) and s[self.count+1] == b:
                self.count += 2
                return 4
            elif self.count+1 < len(s) and  s[self.count+1] == c:
                self.count += 2
                return 9
            tmp = 0
            while self.count+1 < len(s):
                self.count += 1
                if s[self.count] == a:
                    tmp += 1
                else:
                    return tmp + 1
            return tmp + 1
            
            
        if self.count < len(s) and  s[self.count] == b: #5 6 7 8
            tmp = 0
            while self.count+1 < len(s):
                self.count += 1
                if s[self.count] == a:
                    tmp += 1
                else:
                    return tmp + 5
            return tmp+5
        return 0
    def romanToInt(self, s):
        #thousand = self.getInteger('M','','',s)
        if len(s) == 0:
            return 0;
        thousand = 0
        
        if s[0] == 'M':
            self.count += 1
            thousand += 1
        if self.count < len(s) and s[self.count] == 'M':
            self.count += 1
            thousand += 1
        if self.count < len(s) and s[self.count] == 'M':
            self.count += 1
            thousand += 1
        hundred = self.getInteger('C','D','M',s)
        decade = self.getInteger('X','L','C',s)
        unit = self.getInteger('I','V','X',s)
        return 1000 * thousand + 100 * hundred + 10 * decade + unit