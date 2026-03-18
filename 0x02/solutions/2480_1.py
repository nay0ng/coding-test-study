import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

dice = list(map(int, input().split()))
counter = Counter(dice)

value, count = counter.most_common(1)[0] 

if count == 3:
    print(10000 + value * 1000)
elif count == 2:
    print(1000 + value * 100)
else:
    print(max(dice) * 100)