class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(info[11:13]) > 60 for info in details)
