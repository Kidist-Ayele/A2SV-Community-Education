from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        left = right =0
        while right < len(nums):
            res = max(res, right - left)
            if nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            right += 1
        res = max(res, right - left)
        return res

        