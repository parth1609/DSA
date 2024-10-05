class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        total = 0

        final_product = skill[0] + skill[-1]

        for i in range(n//2):
            if skill[i] + skill[-i-1] != final_product:
                return -1
            total += skill[i] * skill[-i-1]

        return total
