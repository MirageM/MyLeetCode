# Leetcode: 268. Missing Number
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = ((len(nums) + 1) * (len(nums))) // 2
        for num in nums:
            total -= num
        return total
   