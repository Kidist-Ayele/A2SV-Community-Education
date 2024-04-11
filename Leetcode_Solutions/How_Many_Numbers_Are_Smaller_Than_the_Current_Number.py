class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]: 
        arr = []
        for i in range(len(nums)):
            count_less = 0
            current_num = nums[i]
            for j in range(0, len(nums)):
                if nums[j] < current_num:
                    count_less += 1
            arr.append(count_less)
        return arr