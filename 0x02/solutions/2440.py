# Authored by : nayoung918
# https://www.acmicpc.net/problem/2440
import sys
input = sys.stdin.readline().rstrip()

n = int(input())

print(*['*'*i for i in range(n, 0, -1)], sep='\n')