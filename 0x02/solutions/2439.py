# Authored by : nayoung918
# https://www.acmicpc.net/problem/2439
import sys
input = sys.stdin.readline

N = int(input())

print(*[' ' * (N-i) + '*' * i for i in range(1, N+1)], sep='\n')

# sys.stdout.write('\n'.join([' '*N-i + '*'*i for i in range(1, N+1)]))