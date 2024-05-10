class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        left = right = 0
        cnt = 0
        players.sort()
        trainers.sort()
        while left < len(players) and right < len(trainers):
            if players[left] <= trainers[right]:
                cnt += 1
                left += 1
                right += 1
            else:
                right += 1
        return cnt
        