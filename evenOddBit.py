# Leetcode Problem 2595: Number of Even and Odd Bits
class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        s = bin(n)[2:][::-1]
        even = 0
        odd = 0
        for i in range(len(s)):
            if i%2==1 and s[i] == '1':
                odd += 1
            if i%2==0 and s[i] == '1':
                even += 1
        return [even, odd]