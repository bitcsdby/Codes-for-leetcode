class Solution:
   
    # @return an integer
    def divide(self, dividend, divisor):
        
        if divisor == 1:
            return dividend
        if divisor == 2:
            return dividend >> 1
        
        sign = 0
        
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
            sign = 0
        elif dividend > 0 and divisor > 0:
            sign = 0
        else:
            if dividend < 0:
                dividend = -dividend
            if divisor < 0:
                divisor = -divisor
            sign = 1
            
        if dividend < divisor:
            return 0
        
        t = 0
        rlt = 0
        
        while (dividend >> t) - (divisor << t) > 0:
                t += 1
        
        
        while t != 0 and dividend - (divisor << t) >= 0:
            dividend -= (divisor << t)
            rlt += 2 << (t-1)
            
        while dividend -divisor >= 0:
            dividend -= divisor
            rlt += 1
            
        if sign == 1 :
            return -rlt
        return rlt