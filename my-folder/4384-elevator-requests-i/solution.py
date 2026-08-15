"""
donate n no floors
0 to n-1
requests is the array you are given ( sequence of floor request)

start = 0
per second 1 floor
request 2 3 1 4 
if it is already in the given floor no request needed
dddd

start = 0
initial variable = requests[0] - start
create a list which is of the second it required = [2 1 3 1]
s.append(ini)
totalsec = 0

for i in range(1, len(requests)):
    maxnum = max(requests[i], requests[i+1])
    minnum = min(requests[i], requests[i+1])
    sum = maxnum - minnum
    s.append(sum)
for num in s:
    totalsec += num

return totalsec
    
"""
class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        start = 0
        initial = requests[0] - start
        s = []
        s.append(initial)
        totalsec = 0
        
        for i in range(len(requests)-1):
            maxnum = max(requests[i], requests[i+1])
            minnum = min(requests[i], requests[i+1])
            sum = maxnum - minnum
            s.append(sum)
        for num in s:
            totalsec += num
        
        return totalsec
        
