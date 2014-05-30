class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        l = s.split(' ')
            
        while len(l) != 0:
            tmp = l.pop()
            if tmp.isalpha():
                return len(tmp)
            
        return 0