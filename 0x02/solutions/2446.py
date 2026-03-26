# Authored by : nayoung918
# https://www.acmicpc.net/problem/2446
import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

print(*[' '* i + '*'* (2*(n-i)-1) for i in range(n)], sep='\n')
print(*[' '*(n-i) + '*'*(2*i -1) for i in range(2, n+1)], sep='\n')
