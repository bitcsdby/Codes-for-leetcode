public class Solution {
    public int reverse(int x) {
        if (x == 0)
            return x;
            
        int sign = 1;
        int iret = 0;
        
        if(x < 0){
            sign = -1;
            x = -x;
        }
        
        while(x > 0 ){
            iret = iret * 10 + (x % 10);
            x = x / 10;
        }
        
        return iret * sign;
    }
}