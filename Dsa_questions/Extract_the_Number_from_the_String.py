# Extract the Number from the String


class Solution:
    def ExtractNumber(self,sentence):
        #code here
        nums = sentence.split(" ")
        number = []
        for num in nums:
            if num.isdigit():
                if '9' not in num:
                    number.append(int(num))
        if number:
            return max(number)
        else:
            return -1
