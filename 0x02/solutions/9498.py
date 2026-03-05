# Authored by : nayoung918
# https://www.acmicpc.net/problem/9498
import sys
input = sys.stdin.readline

# Authored by : nayoung918
# https://www.acmicpc.net/problem/9498
import sys
input = sys.stdin.readline

n = int(input())

if n > 89:
    print('A')
elif n > 79:
    print('B')
elif n > 69:
    print('C')
elif n > 59:
    print('D')
else:
    print('F')