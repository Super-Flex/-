import sys

input = sys.stdin.readline

n = int(input())
for i in range(n):
    _ = input()
    l = list(map(int, input().split()))
    ans = 0
    s = 0
    for j in l:
        if j == 1:
            s = 0
        else:
            s += 1
            ans = max(ans, s)
    print(max(ans, s))
