# Leetcode Problem 2656. Maximum Sum With Exactly K Elements
class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return max(nums)*k + k*(k-1)/2