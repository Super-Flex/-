import sys

input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))
s = set(l)
MOD = 10**9 + 7

arr = [0] * k
for i in l:
    arr[i % k] += 1

import math

m = 0
ans = 1
for i in range(k // 2 + 1):
    if i == 0 or i + i == k:
        ans *= arr[i] + 1
    else:
        ans *= pow(2, arr[i], MOD) + pow(2, arr[k - i], MOD) - 1
print((ans - n - 1) % MOD)
