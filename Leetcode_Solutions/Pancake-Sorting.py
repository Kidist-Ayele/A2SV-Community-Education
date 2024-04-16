from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        max_value = len(arr)
        current_last = len(arr) - 1
        for i in range(len(arr)):
            current_index = arr.index(max_value)
            if current_index == current_last:
                current_last -= 1
                max_value -= 1
                continue
            elif current_index == 0:
                arr = list(reversed(arr[:current_last+1])) + arr[current_last+1:]
                result.append(current_last + 1)
                
            else:
                arr = list(reversed(arr[:current_index +1])) + arr[current_index+1:]
                result.append(current_index + 1)
                arr = list(reversed(arr[:current_last+1])) + arr[current_last+1:]
                result.append(current_last+1)
            current_last -= 1
            max_value -= 1
        
        return result
        