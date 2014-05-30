class Solution:
    # @return a string
    def getRoman(self,a,b,c,digit):
        tmp = ''
        if digit == 1:
            tmp += a;
        elif digit == 2:
            tmp += a
            tmp += a
        elif digit == 3:
            tmp += a
            tmp += a
            tmp += a
        elif digit == 4:
            tmp += a
            tmp += b
        elif digit == 5:
            tmp += b
        elif digit == 6:
            tmp += b
            tmp += a
        elif digit == 7:
            tmp += b
            tmp += a
            tmp += a
        elif digit == 8:
            tmp += b
            tmp += a
            tmp += a
            tmp += a
        elif digit == 9:
            tmp += a
            tmp += c
        return tmp
    def intToRoman(self, num):
        lret = ''
        thousand = num / 1000
        if thousand != 0:
            lret += self.getRoman('M','','',thousand);
        hundred = (num % 1000) / 100
        if hundred != 0:
            lret += self.getRoman('C','D','M',hundred);
        decade = (num % 100) / 10
        if decade != 0:
            lret += self.getRoman('X','L','C',decade);
        unit = (num % 10)
        if unit != 0:
            lret += self.getRoman('I','V','X',unit);

        return lret