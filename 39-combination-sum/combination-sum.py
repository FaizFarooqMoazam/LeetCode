class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        
        def dfs(start, path, target_left):
            if target_left == 0:
                res.append(list(path))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target_left:
                    break  
                path.append(candidates[i])
                dfs(i, path, target_left - candidates[i])
                path.pop()
                
        dfs(0, [], target)
        return res