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
