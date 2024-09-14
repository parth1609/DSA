class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        possible_number = ""
        for i in range(len(number)):
            if number[i] == digit:
                possibility = number[:i] + number[i+1:]
                if possibility > possible_number:
                    possible_number = possibility
        return possible_number 
