class Solution:
    def minimumPushes(self, word: str) -> int:
        frq = [0]*26
        for char in word:
            frq[ord(char) - ord('a')] += 1
        frq.sort(reverse=True)

        pushes = 0
        for i in range(26):
            if frq[i] == 0:
                break
            pushes += (i//8 + 1) * frq[i]

        return pushes  

            
