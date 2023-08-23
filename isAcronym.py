# Leetcode Problem 2828: Check if a String is an Acronym of Words
# Time Complexity: O(n) Space Complexity: O(1)
class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        ans = ""
        for word in words:
            ans += word[0]
        return ans == s