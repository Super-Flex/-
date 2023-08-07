# import sys

# input = sys.stdin.readline
# n = int(input())
# l = list(map(int, input().split()))
# m = min(l)
# arr = [0] * 100001
# # for i in l:
# #     arr[i] = 1
# n2 = int(input())
# l2 = list(map(int, input().split()))

# import heapq

# hpush = heapq.heappush
# hpop = heapq.heappop

# q = []
# for i in l:
#     hpush(q, i)
# v = set()
# ans = [0] * 100001
# while q:
#     x = hpop(q)
#     if x in v:
#         continue
#     v.add(x)

#     k = 2
#     while k * x <= 100000:
#         hpush(q, k * x)
#         k += 1
# for i in l2:
#     print(ans[i])

import sys

input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
m = min(l)
arr = [0] * 100001
for i in l:
    arr[i] = 1
n2 = int(input())
l2 = list(map(int, input().split()))

from functools import lru_cache


@lru_cache(None)
def dfs(n):
    if n < m:
        return 0
    ret = arr[n]
    for i in range(2, min(n // 2, int(n ** (1 / 2))) + 1):
        if n % i == 0:
            ret += dfs(n // i)
            if n != i * i:
                ret += dfs(n // (n // i))
    if n != 1 and arr[1]:
        ret += 1
    return ret


for i in l2:
    print(dfs(i), end=" ")
