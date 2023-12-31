# Leetcode Problem 1207: Unique Number of Occurrences
# Time Complexity: O(n^2) Space Complexity: O(1)
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        nums = []
        occurences = []
        for num in arr:
            if num not in nums:
                occurence = arr.count(num)
                if occurence not in occurences:
                    nums += [num]
                    occurences += [occurence]
                else:
                    return False
        return True
