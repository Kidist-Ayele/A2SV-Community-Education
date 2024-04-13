class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        result = ""
        for test in range(len(nums)):
            for i in range(len(nums)-1):
                j = i + 1
                strij = str(nums[i]) + str(nums[j])
                strji = str(nums[j]) + str(nums[i])
                if strji > strij:
                    nums[i] , nums[j] = nums[j], nums[i]
        for i in range(len(nums)):
            result += str(nums[i])
        if result[0] == '0':
            result = "0"
        return result