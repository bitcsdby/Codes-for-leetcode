# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        lret = []
        
        if intervals == []:
            return []
        if len(intervals) == 1:
            return intervals
            
        count = 1
        l = len(intervals)
        
        intervals.sort(key=lambda x:x.start)
        
        newinterval = Interval()
        newinterval.start = intervals[0].start
        newinterval.end = intervals[0].end
        
        while count < l:
            if newinterval.start == intervals[count].start:
                newinterval.end = max(newinterval.end,intervals[count].end)
                count += 1
                continue
            elif newinterval.end >= intervals[count].end:
                count += 1
                continue
            elif newinterval.end >= intervals[count].start:
                newinterval.end = intervals[count].end
            else:
                #tmp = Interval()
                #tmp.start = newinterval.start
                #tmp.end = newinterval.end
                lret.append(newinterval)
                newinterval = intervals[count]
            count += 1
        
        lret.append(newinterval)
        return lret