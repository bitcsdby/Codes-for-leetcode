class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        dict = {}
        
        for x in num:
            dict[x] = 1
        max = -1
        
        for x in num:
            if dict[x] == 1:
                tmp = 1
                dict[x] = -1
                pos = x+1
                while dict.has_key(pos):
                    dict[pos] = -1
                    pos += 1
                    tmp += 1
                pos = x-1
                while dict.has_key(pos):
                    dict[pos] = -1
                    pos -= 1
                    tmp += 1
                if tmp > max:
                    max = tmp
                
        return max
        