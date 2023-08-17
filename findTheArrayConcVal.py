# Leetcode Problem 2562: Find the Array Concatenation Value
# Time Complexity: O(n) Space Complexity: O(1)
class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        concatenation = 0
        while len(nums) > 0:
            if len(nums) > 1:
                concatenation += int(str(nums[0]) +str(nums[-1]))
                del nums[-1]
            else:
                concatenation += nums[0]
            del nums[0]
        return concatenation 