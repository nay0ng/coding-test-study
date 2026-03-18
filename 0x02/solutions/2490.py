# Authored by : nayoung918
# https://www.acmicpc.net/problem/2490
import sys
input = lambda: sys.stdin.readline().rstrip()

result_list = ['D', 'C', 'B', 'A', 'E']

for _ in range(3):
    t = sum(list(map(int, input().split())))
    print(result_list[t])