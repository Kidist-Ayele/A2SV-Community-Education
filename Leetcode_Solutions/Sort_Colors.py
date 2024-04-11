class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            current_min = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[current_min]:
                    current_min = j
            nums[i], nums[current_min] = nums[current_min], nums[i]
        return nums