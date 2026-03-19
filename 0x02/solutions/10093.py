# Authored by : nayoung918
# https://www.acmicpc.net/problem/10093
import sys
input = lambda: sys.stdin.readline().rstrip()

a, b = map(int, input().split())
if b > a:
    a, b = b, a

print(max(0, a-b-1))
print(*list(range(b+1, a)), end=' ')