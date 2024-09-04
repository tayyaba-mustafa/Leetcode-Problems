class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ""
        for i in range(len(s)):
            a = indices.index(i)
            res += s[a]
        return res
