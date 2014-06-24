class Solution:
    # @return an integer
    def maxArea(self, height):
        if height == None:
            return 0;
            
        left = 0;
        right = len(height) - 1;
        
        l = right - left;
        
        max = min(height[left],height[right]) * l;
        
        while left < right: 
            if height[left] < height[right]:
                left += 1;
            else:
                right -= 1;
                
            if max < min(height[left],height[right]) * (right-left):
                max = min(height[left],height[right]) * (right-left);
                
        return max;