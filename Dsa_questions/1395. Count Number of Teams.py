class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0
        for j in range(1,n):
            largerleft = smallerleft = largerright = smallerright = 0

            for i in range(0, j):
                if rating[i] < rating[j]:
                    smallerleft += 1
                elif rating[i] > rating[j]:
                    largerleft += 1
                    

            for k in range(j + 1, n):
                if rating[j] < rating[k]:
                    largerright += 1
                elif rating[j] > rating[k]:
                    smallerright += 1
  
            teams += (largerleft * smallerright)+(smallerleft * largerright)
        

        return teams
