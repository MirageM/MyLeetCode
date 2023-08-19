# Leetcode Problem 2574: Left and Right Sum Differences
# Time Complexity: O(n) Space Complexiy: O(n)
class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            ans.append(abs(sum(nums[:i]) - sum(nums[i+1:])))
        return ans