class Solution:
    # @param height, a list of integer
    # @return an integer
    
    def largestRectangleArea(self, height):
        stack = []
        
        if height == []:
            return 0
        
        height.insert(0,0)
        height.append(0)
        
        iret = 0
        top = -1
        
        for i in range(len(height)):
            if top == -1:
                stack.append(i)
                top += 1
                continue
            
            if height[stack[top]] <= height[i]:
                stack.append(i)
                top += 1
            else:
                while top != -1 and height[stack[top]] > height[i]:
                    icur = stack.pop()
                    top -= 1
                    if (i - stack[top] - 1) * height[icur] > iret:
                        iret = (i - stack[top] - 1) * height[icur]
                stack.append(i)
                top += 1
                        
        return iret