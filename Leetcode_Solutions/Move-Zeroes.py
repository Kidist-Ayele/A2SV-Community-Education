class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[zero_count] = nums[i]
                zero_count += 1
        for i in range(zero_count, n):
            nums[i] = 0
            