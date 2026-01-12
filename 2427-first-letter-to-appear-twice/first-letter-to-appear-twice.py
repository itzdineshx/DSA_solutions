class Solution:
    def repeatedCharacter(self, s: str) -> str:
        S = set()
        for i in s:
            if i not in S:
                S.add(i)
            else:
                return i
        