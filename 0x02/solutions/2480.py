# Authored by : nayoung918
# https://www.acmicpc.net/problem/2480
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
set_dice = set([a, b, c])

if len(set_dice) == 1:
    print(10000 + a*1000)

elif len(set_dice) == 2:
    for i in set_dice:
        if [a, b, c].count(i) == 2:
            print(1000 + i*100)
else:
    print(max([a, b, c]) * 100) 