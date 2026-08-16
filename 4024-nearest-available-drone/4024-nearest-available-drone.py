class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        
        
        result = -1
        mini = float('inf')
        for i in range(len(drones)):
            c = 0
            for j in range(len(drones[i])):
                if j != len(drones[i])-1:
                    c = c + abs(drones[i][j] - target[j])
                if j == len(drones[i])-1: 
                    if drones[i][j] >= c:
                        if c < mini:
                            mini = c
                            result = i
                    
                    
                    
                        
        return result
                
                
        