# Leetcode Problem 2566. Maximum Difference by Remapping a Digit
# Time Complexity: O(n) Space Complexity: O(1)
class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        num1 = str(num)
        for i in range(len(num1)):
            if(num1[i] != '9'):
                max1 = num1.replace(num1[i], '9')
                break
            else:
                max1 = num1
        min1 = num1.replace(num1[0], '0')
        c, d = int(max1), int(min1)
        return c - d
