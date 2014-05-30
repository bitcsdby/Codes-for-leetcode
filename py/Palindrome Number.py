class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        
        if x < 0:
            return False;
            
        if x < 10:
            return True
        
        
        digit_num = 1
        while x / digit_num >= 10:
            digit_num = digit_num * 10;
        
        if x == digit_num:
            return False;
        
        while x != 0:
            l = x % 10;
            h = x / digit_num;
            
            if l != h:
                return False;
                
            x = (x % digit_num) / 10
            digit_num /= 100
        
        return True