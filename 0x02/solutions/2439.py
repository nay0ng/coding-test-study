# Authored by : nayoung918
# https://www.acmicpc.net/problem/2439
import sys
input = sys.stdin.readline

N = int(input())

print(*[' ' * (N-i) + '*' * i for i in range(1, N+1)], sep='\n')

# sys.stdout.write('\n'.join([' '*N-i + '*'*i for i in range(1, N+1)]))

# # Version 1 - 공백 + 별

# n = int(input())
# print(*[" " * (n - i) + "*" * i for i in range(1, n + 1)], sep="\n")


# # Version 2 - f-string 정렬

# n = int(input())
# print(*[f"{'*' * i:>{n}}" for i in range(1, n + 1)], sep="\n")


# # Version 3 - rjust

# n = int(input())
# print(*[("*" * i).rjust(n) for i in range(1, n + 1)], sep="\n")