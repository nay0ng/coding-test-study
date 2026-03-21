# Authored by : nayoung918
# https://www.acmicpc.net/problem/2442
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

# version 1. 공백 이용
print(*[" " * (n-i) + "*"*(2*i - 1) for i in range(1, n+1)], sep='\n')

# version 2. f-string 이용
print(*[f"{'*'*i:>{n}}{'*'*(i-1)}" for i in range(1,n+1)], sep='\n')

# version 3. rjust 이용
print(*[('*'*i).rjust(n)+'*'*(i-1) for i in range(1, n+1)], sep='\n')