import sys

input = sys.stdin.readline

n = int(input())
q = list(map(int, input().split()))
import heapq

heapq.heapify(q)
ans = 1e18
maxn = max(q)
stop = max(q)
while q[0] < stop:
    minn = heapq.heappop(q)
    ans = min(ans, maxn - minn)
    maxn = max(maxn, minn * 2)
    heapq.heappush(q, minn * 2)
print(ans)
