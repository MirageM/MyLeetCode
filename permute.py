# LeetCode Problem: 46. Permutations
class Solution(object):
       def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recursive(num, perm=[], res=[]):
            if len(num) == 0:
                res.append(perm)
            for i in range(len(num)):
                recursive(num[:i] + num[i+1:], perm + [num[i]], res)
            return res
        return recursive(nums)

