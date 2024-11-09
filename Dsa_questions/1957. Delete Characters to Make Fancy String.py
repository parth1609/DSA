class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        k = 1
        for i in range(1,len(s)):
            if s[i] == ans[-1]:
                k+=1
                if k < 3:
                    ans += s[i]
            else:
                k =1
                ans += s[i]
        return ''.join(ans)
