import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
for ___ in range(n):
    a, b = map(int, input().split())
    l = [[] for i in range(a + 1)]
    for __ in range(b):
        x, y = map(int, input().split())
        l[x].append(y)
        l[y].append(x)

    c = Counter([len(i) for i in l])
    l = sorted(c.items(), key=lambda x: (-x[1]))
    arr = []
    for e, cnt in l:
        if e != 0:
            arr.append(cnt)
    arr.sort(reverse=True)

    if len(arr) == 2:
        print(arr[1] - 1, arr[0] // (arr[1] - 1))
    else:
        print(arr[1], arr[0] // arr[1])
