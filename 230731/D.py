import sys
import math

input = sys.stdin.readline

_ = int(input())
for __ in range(_):
    n = int(input())
    l = list(map(int, input().split()))
    arr = [l[0]] + [b - a for a, b in zip(l, l[1:])]
    s1 = set([i + 1 for i in range(n)])
    s2 = set(arr)
    s3 = s1 & s2
    s4 = s1 - s3
    s5 = s2 - s3
    if len(s4) == 1 and len(s5) == 0:
        print("YES")
    elif len(s4) == 2 and len(s5) == 1 and sum(s4) == sum(s5):
        print("YES")
    elif len(arr) == 1 + len(s2) and sum(arr) - sum(s2) == sum(s4) and len(s4) == 2:
        print("YES")
    else:
        print("NO")
