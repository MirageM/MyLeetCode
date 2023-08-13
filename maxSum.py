# Leetcode Problem 2815: Max Pair Sum in an Array
# Time Complexity: O(n) Space Complexity: O(1)
class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_by_digit = defaultdict(int)
        max_sum = -1
        for num in nums:
            digit = max(str(num))
            if digit in max_by_digit:
                max_sum = max(max_sum, max_by_digit[digit] + num)
            max_by_digit[digit] = max(max_by_digit[digit], num)
        return max_sum
