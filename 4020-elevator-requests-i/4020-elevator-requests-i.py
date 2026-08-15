class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        count_time = 0
        previous = 0
        for i in range(len(requests)):
            if requests[i] == 0:
                count_time = count_time + previous
                previous = requests[i]
                
            elif i == 0:
                count_time = count_time + requests[i]
                previous = requests[i]
            elif previous > requests[i]:
                count_time = count_time + (previous - requests[i])
                previous = requests[i]
            elif previous < requests[i]:
                count_time = count_time + (requests[i] - previous)
                previous = requests[i]
            
                

        return count_time 
            
        