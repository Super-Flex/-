import sys
import math

input = sys.stdin.readline

_ = int(input())
for __ in range(_):
    n = input().split()
    l = list(map(int, input().split()))
    l2 = sorted(l)
    for a, b in zip(l, l2):
        if a % 2 != b % 2:
            break
    else:
        print("YES")
        continue
    print("NO")
