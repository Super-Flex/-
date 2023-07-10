import sys

input = sys.stdin.readline


T = int(input())
for _ in range(T):
    n, m, h = map(int, input().split())
    r = 0
    q = []
    for _ in range(n):
        l = list(map(int, input().split()))

        l.sort()
        time = 0
        pnt = 0
        cnt = 0
        for i in l:
            if time + i <= h:
                time += i
                pnt += time
                cnt += 1
        q.append([-cnt, pnt, _ + 1])
        if _ == 0:
            r = q[-1]
    q.sort()
    print(q.index(r) + 1)
