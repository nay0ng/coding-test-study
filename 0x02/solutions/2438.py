# Authored by : nayoung918
# https://www.acmicpc.net/problem/2438
import sys
input = sys.stdin.readline

N = int(input())

# for i in range(1, N+1):
#     sys.stdout.write('*'*i+'\n')

# # 방법 1 - sys.stdout.write + join
# sys.stdout.write("\n".join("*" * i for i in range(1, N + 1)))

# 방법 2 - print + * 언패킹
print(*["*" * i for i in range(1, N + 1)], sep="\n")