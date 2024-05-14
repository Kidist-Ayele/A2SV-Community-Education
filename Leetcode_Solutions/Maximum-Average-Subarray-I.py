from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        left = k
        while left < len(nums):
            current_sum += nums[left] - nums[left - k]  
            max_sum = max(max_sum, current_sum)
            left += 1
        
        return max_sum / k