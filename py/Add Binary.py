class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if a == '0':
            return b
        if b == '0':
            return a
        
        lista = list(a)
        listb = list(b)
        
        lista.reverse()
        listb.reverse()
        
        la = len(lista)
        lb = len(listb)
        lret = []
        
        count = 0
        c = 0
        while count < la and count < lb:
            if int(lista[count])+int(listb[count]) + c >= 2:
                lret.append(str((int(lista[count])+int(listb[count]) + c)%2))
                c = 1
            else:
                lret.append(str(int(lista[count])+int(listb[count])+c))
                c = 0
            count += 1
            
        while count < la:
            if int(lista[count]) + c == 2:
                lret.append('0')
                c = 1
            else:
                lret.append(str(int(lista[count])+c))
                c = 0
            count += 1
        while count < lb:
            if int(listb[count]) + c == 2:
                lret.append('0')
                c = 1
            else:
                lret.append(str(int(listb[count])+c))
                c = 0
            count += 1
            
        if c == 1:
            lret.append('1')
            
        lret.reverse()
        
        return ''.join(lret)