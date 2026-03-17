# Authored by : nayoung918
# https://www.acmicpc.net/problem/2752
import sys
input = sys.stdin.readline

num_list = list(map(int, input().split()))

# num_list = sorted(num_list)
num_list.sort(reverse=False) # 오름차순

print(*num_list)