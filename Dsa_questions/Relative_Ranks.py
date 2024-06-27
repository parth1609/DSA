# 506 .Relative Ranks

class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        rank_mapping = {}
        result = []
        sorted_scores = sorted(scores, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i, score in enumerate(sorted_scores):
            if i < 3:
                rank_mapping[score] = medals[i]
            else:
                rank_mapping[score] = str(i+1)
        for s in scores:
            result.append(rank_mapping[s])

        return result 

