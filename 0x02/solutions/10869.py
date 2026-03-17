# Authored by : nayoung918
# https://www.acmicpc.net/problem/10869
import sys
input = lambda: sys.stdin.readline().rstrip()

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)