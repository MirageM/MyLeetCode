# LeetCode Problem 242. Valid Anagram
# Time Complexity: O(n) Space Complexity: O(n)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        one = Counter(s)
        two = Counter(t)
        return one == two