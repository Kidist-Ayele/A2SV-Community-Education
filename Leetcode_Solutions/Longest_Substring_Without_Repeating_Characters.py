class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = left  = 0
        max_cnt = 0
        char_set = set()
        while right < len(s):

            if s[right] not in char_set:
                char_set.add(s[right])
                max_cnt = max(max_cnt,  right - left + 1)
                right += 1
            else:
                char_set.remove(s[left])
                left += 1
      
        return max_cnt
        