class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        cnt = 0
        n = len(people)
        left , right = 0, n - 1
        people.sort()
        while left < right:
            if (people[left] + people[right]) > limit:
                cnt += 1
                right -= 1
                n -= 1
            else:
                cnt += 1
                left += 1
                right -= 1
                n -= 2
        if n == 1:
            cnt += 1
        return cnt
