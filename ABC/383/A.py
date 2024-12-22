n = int(input())
events = []
for i in range(n):
    t, v = map(int,input().split())
    events.append((t,v))

current_water = 0
current_time = 0

for t,v in events:
    time_passed = t - current_time
    current_water = max(0, current_water - time_passed)
    current_water += v
    current_time = t

print(current_water)