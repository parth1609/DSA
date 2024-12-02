class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        splited_word = sentence.split()
        for i in range(len(splited_word)):
            if splited_word[i].startswith(searchWord):
                return i+1
        return -1
