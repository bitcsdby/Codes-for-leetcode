class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def __init__(self):
        self.lret = []
    def dfs(self,solution,candidates,target):
        lret = []
        tmpsum = 0
        for x in solution:
            tmpsum += x
        
        if tmpsum == target:
            return [solution]
        if tmpsum > target:
            return []
        if candidates == []:
            return []
        
        num = 0
        ltmp = []
        while tmpsum + candidates[0] <= target:
            tmpsum += candidates[0]
            num += 1
            for i in range(len(candidates)):
                if candidates[i+1:] != [] or len(candidates) == 1:
                    ltmp = self.dfs(solution+[candidates[0]]*num,candidates[i+1:],target)
                    if ltmp != []:
                        lret += ltmp
                if i != len(candidates)-1 and tmpsum + candidates[i+1] > target:
                    break
        return lret
        
    def combinationSum(self, candidates, target):
        candidates.sort()
        lret = []
        for i in range(len(candidates)):
            lret += self.dfs([],candidates[i:],target)
        
        return lret