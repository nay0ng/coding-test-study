# Authored by : nayoung918
# https://www.acmicpc.net/problem/15552
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    # 불필요한 list()
	# print(sum(list(map(int, input().split()))))

	# 개선
	print(sum(map(int, input().split())))  # sum()은 iterable 바로 받음