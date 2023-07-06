#LeetCode Problem: 39. Combination Sum
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(target, path, start):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                dfs(target - candidates[i], path + [candidates[i]], i)
        dfs(target, [], 0)
        return res
