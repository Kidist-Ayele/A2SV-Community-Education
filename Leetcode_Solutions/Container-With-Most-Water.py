class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = []
        left, right = 0 , len(height) - 1
        while left < right:
            if height[left] < height[right]:
                width = height[left] * (right - left)
                result.append(width)
                left += 1
            elif height[left] == height[right]:
                width = height[left] * (right - left)
                result.append(width)
                left += 1
                right -= 1
            else:
                width = height[right] * (right - left)
                result.append(width)
                right -= 1
        return max(result)