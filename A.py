import sys

input = sys.stdin.readline

n = int(input())
for i in range(n):
    x = input().strip()
    ans = 0
    for a, b in zip(x, "codeforces"):
        if a != b:
            ans += 1
    print(ans)
