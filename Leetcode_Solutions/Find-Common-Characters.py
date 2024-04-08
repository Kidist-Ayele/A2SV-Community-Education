class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        x = len(words)
        common = Counter(words[0])
        for i in range(1, x):
            common &= Counter(words[i])
        return list(common.elements())
        