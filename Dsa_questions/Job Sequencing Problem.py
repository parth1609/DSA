'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        # code here
        Jobs.sort(key = lambda x: x.profit, reverse=True)
        max_deadline  = max(Job.deadline for Job in Jobs)
        
        slots = [-1] * (max_deadline + 1)
        
        count_jobs = 0
        max_profits = 0
        
        for job in Jobs:
            for slot in range(min(job.deadline, max_deadline),0,-1):
                if slots[slot] == -1:
                    slots[slot] = job.id
                    count_jobs +=1
                    max_profits += job.profit
                    break
        
        return [count_jobs, max_profits]
