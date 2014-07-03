class Solution:
    # @return a list of strings, [s1, s2]
        
    def letterCombinations(self, digits):
        dic = {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        lret = [""]
        
        for d in digits:
            ltmp = []
            for letter in dic[d]:
                if lret == []:
                    ltmp.append(letter)
                else:
                    for x in lret:
                        ltmp.append(x+letter)
            lret = ltmp[:]
            
        return lret