# Authored by : nayoung918
# https://www.acmicpc.net/problem/2752
# 정렬이 아닌 수학 계산으로 구현
import sys
input = sys.stdin.readline

num_list = list(map(int, input().split()))

min_num = min(num_list)
max_num = max(num_list)

print(min_num, sum(num_list)-min_num-max_num, max_num)