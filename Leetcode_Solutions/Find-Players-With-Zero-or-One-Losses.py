from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = defaultdict(int)
        losers = defaultdict(int)
        for winner, loser in matches:
            winners[winner] += 1
            losers[loser] += 1
        ans = []
        player = []
        for key, value in winners.items():
            if losers[key] == 0:
                player.append(key)
        player.sort()
        ans.append(player)
        player = []
        for key, value in losers.items():
            if losers[key] == 1:
                player.append(key)
        player.sort()
        ans.append(player)

        return ans 
        