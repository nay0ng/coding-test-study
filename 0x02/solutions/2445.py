# Authored by : nayoung918
# https://www.acmicpc.net/problem/2445
import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())

print(*['*' * i + ' ' * 2 * (n-i) + '*' * i for i in range(1, n+1)], sep='\n')
print(*['*' * i + ' ' * 2 * (n-i) + '*' * i for i in range(n-1, 0, -1)], sep='\n')