# Authored by : nayoung918
# https://www.acmicpc.net/problem/2562
import sys
input = lambda: sys.stdin.readline().rstrip()

num_list = list(map(int, [input() for _ in range(9)]))
max_num = max(num_list)
print(max_num)
print(num_list.index(max_num)+1)