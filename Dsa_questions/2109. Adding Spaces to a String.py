class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        m = len(spaces)
        result = ""
        j = 0
        for i in range(n):
            if j<m and i == spaces[j]:
                result += " "
                j+=1
            result += s[i]
        return result
