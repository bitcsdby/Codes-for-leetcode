/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */

 // O(n^2 logn)
class Solution {
public:
    int maxPoints(vector<Point> &points) {
        
        int imax = 0;
        
        for(int i = 0;i < points.size();i++)
        {
            int same = 1;
            int vertical = 0;
            map<double,int> slope;
            map<double,int>::iterator si = slope.begin();
            
            for(int j = 0;j < points.size();j++)
            {
                if(j == i)
                    continue;
                
                if(points[i].x == points[j].x)
                {
                    if(points[i].y == points[j].y)
                        same += 1;
                    else
                    {
                        vertical += 1;
                    }
                }
                else
                {
                    double s = ((double)points[i].y - (double)points[j].y) / ((double)points[i].x - (double)points[j].x);
                    if(slope.find(s) == slope.end())
                    {
                        slope[s] = 1;
                    }
                    else
                    {
                        slope[s] += 1;
                    }
                }
            }
            
            for(si = slope.begin();si != slope.end(); ++si)
            {
                if(si->second + same > imax)
                    imax = si->second + same;
            }
            
            if(vertical + same > imax)
                imax = vertical + same;
        }
        
        return imax;
    }
};