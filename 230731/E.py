import sys
import math

input = sys.stdin.readline

_ = int(input())
for __ in range(_):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    k = list(map(int, input().split()))
    edge = [[] for i in range(n + 1)]
    redge = [[] for i in range(n + 1)]
    deg = [0] * (n + 1)
    for i in range(n):
        x = list(map(int, input().split()))
        for j in x[1:]:
            redge[i + 1].append(j)
            edge[j].append(i + 1)
            deg[i + 1] += 1

    dp = [0] + c
    for i in k:
        dp[i] = 0
    from collections import deque

    start = deque([i + 1 for i in range(n) if deg[i + 1] == 0])
    while start:
        now = start.popleft()
        if redge[now]:
            dp[now] = min(dp[now], sum(dp[s] for s in redge[now]))

        for to in edge[now]:
            deg[to] -= 1
            if deg[to] == 0:
                start.append(to)

    print(*dp[1:])
