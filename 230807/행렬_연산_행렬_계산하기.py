import sys

input = sys.stdin.readline

n, m, q = map(int, input().split())
l = []
d = {}
for i in range(q):
    x, y, z = map(int, input().split())
    d[y * (1 if x == 1 else -1)] = d.get(y * (1 if x == 1 else -1), 0) + z
for i in range(n):
    for j in range(m):
        print(d.get(i + 1, 0) + d.get(-j - 1, 0), end=" ")
    print()
