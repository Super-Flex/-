import sys

input = sys.stdin.readline

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    q = [a]
    s = {a}
    while q:
        n = q.pop(0)
        if n == b:
            print("YES")
            break
        if n % 3 == 0:
            if n // 3 not in s:
                q.append(n // 3)
            if n // 3 * 2 not in s:
                q.append(n // 3 * 2)
            s.add(n // 3)
            s.add(n // 3 * 2)
    else:
        print("NO")
