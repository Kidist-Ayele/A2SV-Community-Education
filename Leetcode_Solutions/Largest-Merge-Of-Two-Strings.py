class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = len(word1)
        m = len(word2)
        result = ""
        left = right = 0
        while left < n and right < m:
            if word1[left:] > word2[right:]:
                result += word1[left]
                left += 1
            else:
                 result += word2[right]
                 right += 1
        result += word1[left:] + word2[right:]
        
        return result