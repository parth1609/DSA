class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        string1 = s1.split(" ")
        string2 = s2.split(" ")
        string = string1 + string2
        all_string = Counter(string)
        return [uncomman_word for uncomman_word in all_string if all_string[uncomman_word] ==1 ] 

        
