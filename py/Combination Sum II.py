class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def comsum(self,solution,candidates,target):
        lret = []
        
        if target == 0:
            return [solution]
            
        if candidates[0] == target:
            return [solution+[candidates[0]]]
        
        if candidates[0] > target:
            return []
            
        for j in range(1,len(candidates)):
            if candidates[0] + candidates[j] > target:
                break
            if j != 1 and candidates[j] == candidates[j-1]:
                continue
            lret += self.comsum(solution+[candidates[0]],candidates[j:],target-candidates[0])    
        
        return lret
            
            
    def combinationSum2(self, candidates, target):
        candidates.sort()
        lret = []
        
        for i in range(len(candidates)):
            if i != 0 and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] == target:
                lret += [[candidates[i]]]
                break
            if candidates[i] > target:
                break
            lret += self.comsum([],candidates[i:],target)
        
        return lret