import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    ans = 0
    t = int(input())
    for __ in range(t):
        a, b = map(int, input().split())
        if a - b > 0:
            ans += 1
    print(ans)
