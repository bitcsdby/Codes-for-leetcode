class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def justify(self,lwords,tmplenth,L):
        if len(lwords) == 1:
            return lwords[0] + ' ' * (L-tmplenth)
        nwords = len(lwords)
        nspaces = L - tmplenth
        
        space = nspaces / (nwords-1)
        space_mod = nspaces % (nwords - 1)
        
        sret = lwords[0]
        
        for i in range(1,len(lwords)):
            sret += ' ' * space
            if space_mod != 0:
                sret += ' '
                space_mod -= 1
            sret += lwords[i]
        
        return sret
        
        
    def fullJustify(self, words, L):
        lret = []
        
        if L == 0:
            return words
        
        lcurstr = []
        tmplenth = 0
        i = 0
        while i < len(words):
            if tmplenth + len(lcurstr) + len(words[i]) <= L:
                lcurstr.append(words[i])
                tmplenth += len(words[i])
                i += 1
            else:
                lret.append(self.justify(lcurstr,tmplenth,L))
                tmplenth = 0
                lcurstr = []
        
        lret.append(' '.join(lcurstr) + ' '*(L-tmplenth-len(lcurstr)+1))     
        return lret