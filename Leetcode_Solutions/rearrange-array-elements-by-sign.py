from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr_pos = []
        arr_neg = []
        result_arr = []
        for index in range(len(nums)):
            if nums[index]< 0:
                arr_neg.append(nums[index])
            else:
                arr_pos.append(nums[index])
        for index in range(len(nums) //2):
            result_arr.append(arr_pos[index])
            result_arr.append(arr_neg[index])
        return result_arr