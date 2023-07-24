# LeetCode: 292. Nim Game
# Time Complexity: O(1) Space Complexity: O(1)

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0