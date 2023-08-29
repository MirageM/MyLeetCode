# Leetcode Problem 2544: Alternating Digit Sum
# Time Complexity: O(n) Space Complexity: O(1)
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        count = 0
        n = str(n)
        for i in range(len(n)):
            if i % 2 == 0:
                count += int(n[i])
            else:
                count -= int(n[i])
        return count