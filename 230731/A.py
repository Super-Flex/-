import sys
import math

input = sys.stdin.readline

_ = int(input())
for __ in range(_):
    n, m, k, h = map(int, input().split())
    l = list(map(int, input().split()))
    ans = 0
    for i in l:
        if abs(h - i) % k == 0 and 0 < abs(h - i) // k < m:
            ans += 1
    print(ans)
