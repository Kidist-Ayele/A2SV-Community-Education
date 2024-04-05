from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        double_size = 2 * len(nums)
        for index in range(double_size):
             ans.append(nums[index % len(nums)])
        return ans
        