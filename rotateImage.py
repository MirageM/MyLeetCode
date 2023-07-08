# LeetCode 48. Rotate Image
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
#         # Solution 1: 2D array
#         # Time: O(n^2)
#         # Space: O(n^2)
        n = len(matrix)
        res = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[j][n - i - 1] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = res[i][j]
        return matrix

