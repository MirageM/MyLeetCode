# Leetcode Problem 2600: K Items With The Maximum Sum
# Time Complexity: O(1) Space Complexity: O(1)
class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        a = 2 * numOnes + numZeros - k
        return min(k, numOnes, a)