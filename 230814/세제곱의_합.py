import sys

input = sys.stdin.readline

n = int(input())

print((n * (n + 1)) // 2)
print(((n * (n + 1)) // 2) ** 2)
print(sum([i**3 for i in range(1, 1 + n)]))
