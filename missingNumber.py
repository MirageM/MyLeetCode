# Leetcode: 268. Missing Number
# Time Complexity: O(n) Space Complexity: O(1)
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
   