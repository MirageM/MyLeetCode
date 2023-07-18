# LeetCode Problem 242. Valid Anagram
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