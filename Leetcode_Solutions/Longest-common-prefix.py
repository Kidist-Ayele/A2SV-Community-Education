class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sort_arr = sorted(strs)
        common = ""
        x = len(sort_arr)
        first_element = sort_arr[0]
        last_element = sort_arr[x-1]
        len_first = len(first_element)
        len_last = len(last_element)
        min_num = min(len_first, len_last)

        for i in range(min_num):
            if first_element[i] == last_element[i]:
                common += first_element[i]
            else:
                break
        return common
        