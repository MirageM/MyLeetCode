# Leetcode Problem 2570: Merge Two 2D Arrays by Summing Values
# Time Complexity: O(n) Space Complexity: O(n)
class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        l, r = 0, 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l][0] < nums2[r][0]:
                res.append(nums1[l])
                l += 1
            elif nums1[l][0] > nums2[r][0]:
                res.append(nums2[r])
                r += 1
            else:
                val = nums1[l][1] + nums2[r][1]
                res.append([nums1[l][0], val])
                l, r = l + 1, r + 1
        if l < len(nums1):
            res.extend(nums1[l:])
        elif r < len(nums2):
            res.extend(nums2[r:])
        return res