# Leetcode Problem 2558. Take Gifts From The Richest Pile
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        while k > 0:
            max_pile = max(gifts)
            index = gifts.index(max_pile)
            gifts[index] = int(math.sqrt(max_pile))
            k = k - 1
        return sum(gifts)