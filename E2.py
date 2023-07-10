import sys
import math

input = sys.stdin.readline


def f(r, n):
    return (pow(r, n) - 1) // (r - 1)


T = int(input())
for _ in range(T):
    n = int(input())
    if n < 7:
        print("NO")
        continue
    limit = int(math.log(n, 2)) + 2
    for i in range(3, limit):
        l = 1
        r = int(n ** (1 / (i - 1)) + 1)
        while l + 1 < r:
            mid = (l + r) // 2
            if f(mid, i) < n:
                l = mid
            else:
                r = mid
        if f(r, i) == n:
            print("YES")
            break
    else:
        print("NO")
