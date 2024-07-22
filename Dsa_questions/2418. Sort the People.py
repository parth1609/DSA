class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipp = list(zip(names,heights))
        zipp.sort(reverse=True, key = lambda x: x[1])
        sort_names = [name for name,height in zipp]
        return sort_names
