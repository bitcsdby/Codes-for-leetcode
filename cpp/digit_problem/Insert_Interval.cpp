/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
        intervals.push_back(newInterval);
        
        sort(intervals.begin(),intervals.end(),[](const Interval &a, const Interval & b){return a.start < b.start;});
        
        vector<Interval> vret;
        
        if(intervals.size() == 0)
            return vret;
        
        vret.push_back(intervals[0]);
        
        for(int i = 1;i < intervals.size();i++)
        {
            if(intervals[i].start > (*(vret.end()-1)).end)
                vret.push_back(intervals[i]);
            else if(intervals[i].start <= (*(vret.end()-1)).end)
                (*(vret.end()-1)).end = (*(vret.end()-1)).end > intervals[i].end ? (*(vret.end()-1)).end : intervals[i].end;
        }
        
        return vret;
    }
};