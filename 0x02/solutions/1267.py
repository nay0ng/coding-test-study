# Authored by : nayoung918
# https://www.acmicpc.net/problem/1267
import sys
input = lambda: sys.stdin.readline().rstrip()

call_count = int(input())
call_minute = list(map(int, input().split()))

Y = 0
M = 0

for i in call_minute:
    Y += (i // 30 + 1) * 10 
    M += (i // 60 + 1) * 15

if Y < M:
    print(f"Y {Y}")
elif M < Y:
    print(f"M {M}")
else:
    print(f"Y M {Y}")