# Authored by : nayoung918
# https://www.acmicpc.net/problem/10808
import sys
input = lambda: sys.stdin.readline().rstrip()

word = input()
cnt_list = [0] * 26

for w in word:
    idx = ord(w) - ord('a')
    cnt_list[idx] += 1

print(*cnt_list, sep=' ')