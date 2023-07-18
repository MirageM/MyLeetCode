class Solution(object):
    def isAnagram(self, s, t):
        for i in range(len(s)):
            if s[i] not in t:
                return False
        return True