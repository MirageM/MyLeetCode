# LeetCode Problem: 448. Find All Numbers Disappeared in an Array
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        missing = []
        for i in range(len(nums)):
            if nums[i] > 0:
                missing.append(i + 1)
        return missing
                





    # def findDisappearedNumbers(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     res = []
    #     for i in range(1, len(nums) + 1):
    #         if i not in nums:
    #             res.append(i)
    #     return res
