import sys

input = sys.stdin.readline

n = int(input())
for i in range(n):
    _ = int(input())
    l = [1e9] * 4
    for j in range(_):
        # l.append(list(input().split()))
        x, y = list(input().split())
        arr = {"00": 0, "01": 1, "10": 2, "11": 3}
        l[arr[y]] = min(l[arr[y]], int(x))
    t = min(l[1] + l[2], l[3])
    print(t if t != 1e9 else -1)
