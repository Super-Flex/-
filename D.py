import sys

input = sys.stdin.readline


T = int(input())
for _ in range(T):
    n, d, h = map(int, input().split())
    l = list(map(int, input().split()))[::-1]
    ans = d * h / 2
    pre = l[0]
    for i in l[1:]:
        ud = d * ((h - min(h, pre - i)) / h)
        ans += min(h, pre - i) * (ud + d) / 2
        pre = i
    print(ans)
