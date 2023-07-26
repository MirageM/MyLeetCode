class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.original = list(nums)

    def reset(self):
        """
        :rtype: List[int]
        """
        self.nums = list(self.original)
        return self.nums


    def shuffle(self):
        """
        :rtype: List[int]
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()