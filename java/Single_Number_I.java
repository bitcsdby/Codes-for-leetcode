public class Solution {
    public int singleNumber(int[] A) {
        int iret = 0;
        for(int i: A)
        {
            iret = iret ^ i;
        }
        return iret;
    }
}