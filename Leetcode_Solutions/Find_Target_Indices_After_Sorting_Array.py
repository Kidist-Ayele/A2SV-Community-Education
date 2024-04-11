class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            current_min = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[current_min]:
                    current_min = j
            nums[i], nums[current_min] = nums[current_min], nums[i]
        for i in range(len(nums)):
            if nums[i] == target:
                arr.append(i)
        return arr