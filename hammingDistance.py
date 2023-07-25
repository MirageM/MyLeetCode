# Leetcode: 461. Hamming Distance
# Time Complexity: O(1) Space Complexity: O(1)
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return str(bin(x^y)).count('1')