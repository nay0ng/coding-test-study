# Authored by : nayoung918
# https://www.acmicpc.net/problem/2442
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

# version 1. 공백 문자 사용
print(*[' ' * (n-i) + '*'*(i) for i in range(n, 0, -1)], sep='\n')

# # version 2. rjust() 함수 사용
# print(*[('*' * i).rjust(n) for i in range(n, 0, -1)], sep='\n')

# # version 3. f-string 사용
# print(*[f"{'*'*i:>{n}}" for i in range(n, 0, -1)], sep='\n')