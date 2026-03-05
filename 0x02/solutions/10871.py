# Authored by : nayoung918
# https://www.acmicpc.net/problem/10871
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
num_list = list(map(int, input().split()))

for i in range(n):
    if num_list[i] < x:
        print(num_list[i], end=' ')