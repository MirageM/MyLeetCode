# Leetcode Problem 463. Island Perimeter
# Time Complexity: O(n^2) Space Complexity: O(1)
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        perimeter = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        return perimeter