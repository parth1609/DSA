# 826. Most Profit Assigning Work

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [(difficulty[i],profit[i]) for i in range(len(difficulty))]
        jobs.sort() # sort based on  difficulty
        worker.sort()

        maximum_profit = 0
        maximum_profit_will_be  = 0
        jobs_index = 0

        for abality in worker:
            while jobs_index < len(jobs) and jobs[jobs_index][0] <= abality:
                maximum_profit_will_be = max(maximum_profit_will_be,jobs[jobs_index][1])
                jobs_index+=1
            maximum_profit += maximum_profit_will_be
        
        return maximum_profit


        
