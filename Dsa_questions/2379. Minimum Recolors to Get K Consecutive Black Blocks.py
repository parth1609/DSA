class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        mincolor = k
        kurr = 0
        for i in range(k):
            if blocks[i]=='W':
                kurr+=1
        mincolor = kurr
        for i in range(k,n):
            if blocks[i-k]=='W':
                kurr-=1
            if blocks[i]=='W':
                kurr+=1
            mincolor = min(mincolor,kurr)
        return mincolor
