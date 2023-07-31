import sys
import math

input = sys.stdin.readline

_ = int(input())
for __ in range(_):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    if k == 1:
        print("YES")
        continue
    elif l[0] == l[-1]:
        if l.count(l[0]) >= k:
            print("YES")
            continue
    elif l.count(l[0]) >= k and l.count(l[-1]) >= k:
        n1 = [i for i in range(n) if l[i] == l[0]]
        n2 = [i for i in range(n) if l[i] == l[-1]]
        if n1[k - 1] < n2[-k]:
            print("YES")
            continue
    print("NO")
