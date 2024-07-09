class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_wait_time = 0
        current_time = 0
        
        for order in customers:
            arrival_time = order[0]
            cook_time = order[1]

            if current_time < arrival_time:
                 current_time = arrival_time 

            wait_time = current_time + cook_time - arrival_time
            total_wait_time += wait_time

            current_time += cook_time
        return total_wait_time/len(customers)

