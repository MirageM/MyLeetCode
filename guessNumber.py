# Leetcode problem: 374. Guess Number Higher or Lower
# Time Complexity: O(logn) Space Complexity: O(1)

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = n 
        l = 1
        while l <= r:
            mid = (l + r) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                r = mid - 1
            else:
                l = mid + 1                
       