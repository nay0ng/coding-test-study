# Authored by : nayoung918
# https://www.acmicpc.net/problem/1000
import sys
# input = sys.stdin.readline

# def input():
#     return sys.stdin.readline().rstrip()

# 혹은 lambda로 더 간단하게 쓸 수도 있음
input = lambda: sys.stdin.readline().rstrip()

A, B = map(int, input().split())
print(A + B)