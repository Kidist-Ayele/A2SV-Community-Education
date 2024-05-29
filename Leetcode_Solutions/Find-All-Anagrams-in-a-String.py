from typing import Counter, List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        l = len(p)

        if n < l:
            return []
        
        left, right = 0, l - 1
        ans = []
        res = ""
        count_s = Counter(s[:l - 1])
        count_p = Counter(p)
        while right < n and left <= n - l :
            res = s[left:right + 1]
            count_r = Counter(res)
            
            if count_r == count_p:
                ans.append(left)
               
            left += 1
            right += 1
        return ans

        