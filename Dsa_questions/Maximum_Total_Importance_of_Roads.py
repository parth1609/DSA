# 2285. Maximum Total Importance of Roads

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        result =0 
        cost= 1
        connections = [0] * n
        for road in roads:
            connections[road[0]] += 1
            connections[road[1]] += 1
        
        connections.sort()
        for connection in connections:
            result += connection * cost
            cost += 1
        
        return result 


        
