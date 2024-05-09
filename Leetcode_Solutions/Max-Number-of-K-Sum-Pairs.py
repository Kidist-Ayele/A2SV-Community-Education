class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        cnt = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if (nums[left] + nums[right]) == k:
                cnt += 1
                right -= 1
                left += 1
            elif (nums[left] + nums[right]) > k:
                right -= 1
            else:
                left += 1
        return cnt