# Authored by : nayoung918
# https://www.acmicpc.net/problem/10804
import sys
input = lambda:sys.stdin.readline().rstrip()

num_list = list(range(1, 21))

for _ in range(10):
    a, b = map(int, input().split())

    # temp = num_list[a-1:b]
    # temp.reverse()
    # num_list[a-1:b] = temp

    num_list[a-1:b] = list(reversed(num_list[a-1:b]))

    # for i in list(reversed(num_list[a-1:b])):
    #     num_list[p] = i
    #     p += 1


print(*num_list)