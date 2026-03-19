# Authored by : nayoung918
# https://www.acmicpc.net/problem/15552
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    print(sum(list(map(int, input().split()))))