class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        result = []
        n = len(spaces)
        result.append(s[:spaces[0]])
        for i in range(n-1):
            result.append(s[spaces[i]:spaces[i+1]])
        result.append(s[spaces[n-1]:])
        return ' '.join(result)
