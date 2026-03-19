# Authored by : nayoung918
# https://www.acmicpc.net/problem/2576
import sys
input = lambda: sys.stdin.readline().rstrip()

total_odd = 0
min_odd = 100

for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        total_odd += n
        if min_odd > n:
            min_odd = n
    
if total_odd == 0:
    print(-1)
else:
    print(total_odd)
    print(min_odd)
