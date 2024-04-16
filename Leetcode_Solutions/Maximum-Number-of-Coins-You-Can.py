from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left = 0
        ans = 0
        right = len(piles) - 2
        while left < right:
            ans += piles[right]
            right -= 2
            left += 1
        return ans
        