class Solution {
public:
    void getnext(int* next,const char* needle)
    {
        int i = 0;
        int j = -1;
        
        next[0] = -1;
        int l  = strlen(needle);
        
        while(i < l - 1)
        {
            if(j == -1 || needle[i] == needle[j])
            {
                i += 1;
                j += 1;
                next[i] = j;
            }
            else
                j = next[j];
        }
    }
    char *strStr(char *haystack, char *needle) {
        int *next = new int[strlen(needle)];
        
        getnext(next,needle);
        
        int i = 0;
        int j = 0;
        
        int h = strlen(haystack);
        int n = strlen(needle);
        
        while(j < n && i < h)
        //while((j < strlen(needle)) && (i < strlen(haystack)))
        {
            if(j == -1 || haystack[i] == needle[j])
            {
                i += 1;
                j += 1;
            }
            else
                j = next[j];
        }
        
        if(j == strlen(needle))
            return haystack + i - j;
        else
            return NULL;
    }
        
};