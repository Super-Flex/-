import sys

input = sys.stdin.readline


def check(arr):
    if arr[0] == arr[1] == arr[2] != ".":
        return arr[0]
    return False


T = int(input())
for _ in range(T):
    l = []
    for i in range(3):
        l.append(input().strip())
    flag = True
    for row in l:
        if check(row) and flag:
            print(check(row))
            flag = False
    for column in zip(*l):
        if check(column) and flag:
            print(check(column))
            flag = False
    if check([l[0][0], l[1][1], l[2][2]]) and flag:
        print(l[0][0])
        flag = False
    if check([l[2][0], l[1][1], l[0][2]]) and flag:
        print(l[1][1])
        flag = False
    if flag:
        print("DRAW")
