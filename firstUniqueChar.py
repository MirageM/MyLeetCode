# LeetCode: 387. First Unique Character in a String
# Time Complexity: O(n) Space Complexity: O(n)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hset = collections.Counter(s)
        for i in range(len(s)):
            if hset[s[i]] == 1:
                return i
        return -1