class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                return True
            i += 1
            if nums[0] == nums[len(nums)-1]:
                return True
        return False