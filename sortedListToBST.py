# LeetCode Problem 109. Convert Sorted List to Binary Search Tree
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity: O(nlogn) Space Complexity: O(logn)
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        self.head = head
        def recursive(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            left = recursive(start, mid - 1)
            root = TreeNode(self.head.val)
            self.head = self.head.next
            root.left = left
            root.right = recursive(mid + 1, end)
            return root
        return recursive(0, n - 1)

