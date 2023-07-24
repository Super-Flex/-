import sys

input = sys.stdin.readline

n = int(input())
for ___ in range(n):
    a, b = map(int, input().split())
    l = []
    for i in range(a):
        l.append(list(map(int, input().split())))
    v = set()
    ans = 0
    for i in range(a):
        for j in range(b):
            if (i, j) in v or l[i][j] == 0:
                continue
            tmp = 0
            q = [(i, j)]
            v.add((i, j))
            while q:
                x, y = q.pop(0)
                tmp += l[x][y]
                for nx, ny in (x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1):
                    if (
                        0 <= nx < a
                        and 0 <= ny < b
                        and (nx, ny) not in v
                        and l[nx][ny] != 0
                    ):
                        q.append((nx, ny))
                        v.add((nx, ny))
            ans = max(ans, tmp)
    print(ans)
