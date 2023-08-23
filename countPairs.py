# Leetcode Problem 2824: Count Pairs Whose Sum is Less than Target
# Time Complexity: O(nlogn) Space Complexity: O(1)
class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count