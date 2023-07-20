# Leetcode problem: 258. Add Digits

# Time Complexity: O(1) Space Complexity: O(1)
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9



# Time Complexity: O(n) Space Complexity: O(1)
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def oneDigit(sum, num_str):
            for i in range(len(num_str)):
                sum = sum + eval(num_str[i])
            if len(str(sum)) >= 2:
                return oneDigit(0, str(sum))
            else:
                return sum
        sum = 0
        num_str = str(num)
        return oneDigit(sum, num_str)
