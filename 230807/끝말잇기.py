import sys

input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append(input().strip())
n = int(input())
arr = []
for i in range(n):
    arr.append(input().strip())
for i in range(len(l)):
    if l[i] == "?":
        s, e = "", ""
        if i != 0:
            s = l[i - 1][-1]
        if i != len(l) - 1:
            e = l[i + 1][0]
for i in arr:
    if i not in l and ((s and s == i[0]) or not s) and ((e and e == i[-1]) or not e):
        print(i)
        break
