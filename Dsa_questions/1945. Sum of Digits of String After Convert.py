class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string = ""
        for char in s:
            char_no = ord(char) - ord('a') + 1
            string += str(char_no)
        while k >  0:
            result = 0
            for no in string:
                result += int(no)
            string = str(result) 
            k-=1
        return int(string)

