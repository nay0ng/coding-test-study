# Authored by : nayoung918
# https://www.acmicpc.net/problem/2309
import sys
import itertools
input = lambda: sys.stdin.readline().rstrip()

input_list = [int(input()) for _ in range(9)]

nCr = itertools.combinations(input_list, 7)

for i in nCr:
    if sum(list(i)) == 100:
        print(*sorted(list(i)), sep='\n')
        break