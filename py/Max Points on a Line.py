# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if points == None:
            return 0;
        n = len(points)
        
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        max = 0
        
        times = 1
        
        for i in range(n):
            numx = 1
            numy = 1
            for j in range(i+1,n):
                if points[i].x == points[j].x:
                    numx += 1
                if points[i].y == points[j].y:
                    numy += 1
            if numx > max:
                max = numx
            if numy > max:
                max = numy
                
        
        for i in range(n):
            p1 = points[i]
            times = 0
            ltmp = []
            for j in range(i+1,n):
                p2 = points[j]
                if p1.x != p2.x: #x1 != x2
                    a = float(p1.y-p2.y) / float(p1.x-p2.x)
                    ltmp.append(a)
                if p1.x == p2.x and p1.y == p2.y:
                    times += 1
            
            ltmp.sort()
            
            tmpn = len(ltmp)
            if tmpn == 0:
                continue
            count = 0
            tag = ltmp[0]
            num = 1 + times
            while count < tmpn:
                if ltmp[count] == tag:
                    num += 1
                else:
                    if num > max:
                        max = num
                    num = 2 + times
                    tag = ltmp[count]
                count += 1
                    
            if num > max:
                max = num
                
        return max