# Authored by : nayoung918
# https://www.acmicpc.net/problem/2480
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
set_dice = set([a, b, c])

if len(set_dice) == 1:
    print(10000 + a*1000)

elif len(set_dice) == 2:
    for i in set_dice:
        if [a, b, c].count(i) == 2:
            print(1000 + i*100)
else:
    print(max([a, b, c]) * 100) 

import sys
input = lambda: sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())

# 모두 다 같은 수인 경우
if a == b == c:
    print(10000 + a * 1000)
    
# 두 번째 수와 다른 어떤 한 수가 같은 경우
elif b in (a, c): # 이건 결국 if b == a or b == c:를 줄인 것
    print(1000 + b * 100)
    
# 첫 번째, 세 번째 수가 같은 경우
elif a == c:
    print(1000 + a * 100)
    
# 세 수가 모두 다른 경우
else:
    print(max(a, b, c) * 100)