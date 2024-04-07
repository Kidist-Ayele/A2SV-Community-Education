class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        len_word = len(words)
        sets = [set(word) for word in words]

        for i in range(len_word):
            for j in range(i+1, len_word):
                if sets[i] == sets[j]:
                    count += 1
        return count
        