# Leetcode Problem 2529: Maximum Count of Postive Integer and Negative Integer
# Time Complexity: O(n) Space Complexity: O(1)
class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_len = len(nums)
        pos, neg = 0, 0
        zero_found = False
        if nums[-1] < 0:
            return total_len
        for i in range(total_len):
            if nums[i] > 0:
                pos = total_len - i
                if neg == 0:
                    neg = i
                break
            if nums[i] == 0 and not zero_found:
                neg, zero_found = i, True
        return max(pos, neg)