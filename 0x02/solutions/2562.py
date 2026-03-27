# Authored by : nayoung918
# https://www.acmicpc.net/problem/2562
import sys
input = lambda: sys.stdin.readline().rstrip()

max_num = float("-inf")
idx_num = 0

for i in range(9):
    num = int(input())
    if max_num < num:
        max_num = num
        idx_num = i + 1

print(max_num)
print(idx_num)