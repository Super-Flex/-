import sys, math

input = sys.stdin.readline


def f(r, n):
    return int((pow(r, n) - 1) / (r - 1))


T = int(input())
for _ in range(T):
    n = int(input())
    if n < 7:
        print("NO")
        continue
    for i in range(2, int(math.sqrt(n)) + 1):
        l = 0
        r = int(math.log(n, i)) + 1
        while l + 1 < r:
            mid = int((l + r) // 2)
            if f(i, mid) < n:
                l = mid
            else:
                r = mid
        if f(i, int(r)) == n and r >= 2:
            print("YES")
            break
    else:
        print("NO")


# 1 4 16 =21
# 1 3 9 = 13
# 1 2 4 8 = 15
# 1 2 4 = 7
