class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            index = (columnNumber - 1) % 26
            ans = chr(index + ord('A')) + ans
            columnNumber = (columnNumber - 1) // 26
        return ans
