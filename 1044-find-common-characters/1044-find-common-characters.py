class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return reduce(lambda a, b: a & b, map(Counter, words)).elements()