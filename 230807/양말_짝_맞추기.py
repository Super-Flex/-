import sys

input = sys.stdin.readline

from collections import Counter

l = []
for i in range(5):
    l.append(int(input()))
arr = list(Counter(l).items())
for a, n in arr:
    if n % 2:
        print(a)
        exit(0)
