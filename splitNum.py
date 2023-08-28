# Leetcode Problem 2578: Split With Mimimum Sum
# Time Complexity: O(nlogn) Space Complexity: O(n)
from queue import PriorityQueue

class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = [int(x) for x in str(num)]
        num1 = ""
        num2 = ""
        pq = PriorityQueue()
        for i in a:
            pq.put(i)
        while not pq.empty():
            num1 += str(pq.get())
            if not pq.empty():
                num2 += str(pq.get())
        if num2:
            return int(num1) + int(num2)
        else:
            return int(num1)
