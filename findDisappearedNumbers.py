class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(1, len(nums) + 1):
            if i not in nums:
                res.append(i)
        return res
