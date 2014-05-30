class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        count = len(digits) - 1;
        c = 1;
        l = len(digits);
        
        while count > 0 :
            if digits[count] + c == 10:
                c = 1;
                digits[count] = 0;
            else:
                digits[count] += c;
                c = 0;
            count -= 1;
        
        if digits[count] + c == 10:
            digits[count] = 0;
            digits.insert(0,1);
        else:
            digits[count] += c;
            c = 0;
        return digits;