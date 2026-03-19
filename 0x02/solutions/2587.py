# Authored by : nayoung918
# https://www.acmicpc.net/problem/2587
import sys
import statistics
input = lambda: sys.stdin.readline().rstrip()

num_list = [int(input()) for _ in range(5)]

print(statistics.mean(num_list))
# print(int(sum(num_list) // 5))
print(sorted(num_list)[2])