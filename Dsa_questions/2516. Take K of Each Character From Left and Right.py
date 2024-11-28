class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        letter_count = [0,0,0]
        for char in s:
            letter_count[ord(char) - ord('a')] += 1

        if letter_count[0] < k or letter_count[1] < k or letter_count[2] < k:
            return -1
        
        i = j = 0
        MiddleStringLength = 0
        while i < len(s):
            letter_count[ord(s[i]) - ord('a')] -= 1
            while letter_count[ord(s[i]) - ord('a')] < k:
                letter_count[ord(s[j]) - ord('a')] += 1
                j += 1
            i+=1
            MiddleStringLength  = max(MiddleStringLength, i-j)
        return len(s) - MiddleStringLength
