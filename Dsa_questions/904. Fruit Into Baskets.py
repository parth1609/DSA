class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits)<=2:
            return len(fruits)
        if len(set(fruits)) == 1:
            return len(fruits)
        i=j=0
        maxlen = 0
        unique = {}
        while j<len(fruits):
            if fruits[j] not in unique:
                unique[fruits[j]] = 1
            else:
                unique[fruits[j]] += 1

            if len(unique) == 2:
                maxlen = max(maxlen,j-i+1)
            elif len(unique) > 2:
                while len(unique) > 2:
                    unique[fruits[i]] -=1
                    if unique[fruits[i]] == 0:
                        unique.pop(fruits[i])
                    i+=1
            j+=1
        return maxlen
