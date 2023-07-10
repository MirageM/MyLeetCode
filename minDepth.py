# LeetCode Problem: 111. Minimum Depth of Binary Tree
# Time Complexity: O(n) Space Complexity: O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = [root]
        depth = 1
        rightMost = root
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is None and node.right is None:
                break
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node == rightMost:
                depth += 1
                if node.left is not None:
                    rightMost = node.left
                else:
                    rightMost = node.right
        return depth

                    