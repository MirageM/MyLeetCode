# Leetcode 383. Ransom Note
# Time Complexity: O(n) Space Complexity: O(n)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        str1, str2 = Counter(ransomNote), Counter(magazine)
        if str1 & str2 == str1:
            return True
        return False