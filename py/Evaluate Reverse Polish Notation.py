class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if tokens == None:
            return 0
        
        stack_num = []
        result = 0;
        
        for x in tokens:
            if x == '+':
                second = stack_num.pop()
                first = stack_num.pop()
                stack_num.append(first + second)
            elif x == '-':
                second = stack_num.pop()
                first = stack_num.pop()
                stack_num.append(first - second)
            elif x == '*':
                second = stack_num.pop()
                first = stack_num.pop()
                stack_num.append(first * second)
            elif x == '/':
                second = stack_num.pop()
                first = stack_num.pop()
                
                sign = 0
                if second * first < 0:
                    sign = 1
                if second < 0:
                    second = -second
                if first < 0:
                    first = -first
                if sign == 1:
                    stack_num.append(-(first / second))
                else:
                    stack_num.append( first / second )
            else:
                stack_num.append(int(x))
                
        return stack_num.pop()