class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        n = len(skill)
        left, right = 0, n - 1
        num = skill[left] + skill[right]
        result = 0
        while left < right:
            if (skill[left] + skill[right]) == num:
                result += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1
        return result

        