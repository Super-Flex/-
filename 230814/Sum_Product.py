import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

not1 = [idx for idx in range(n) if arr[idx] != 1]
ts = sum(arr)
ans = n
for i in range(len(not1)):
    s = arr[not1[i]]
    m = arr[not1[i]]
    for j in range(i + 1, len(not1)):
        s += arr[not1[j]] + not1[j] - not1[j - 1] - 1
        m *= arr[not1[j]]
        if m > ts:
            break
        left_1_cnt = not1[0] if i == 0 else not1[i] - not1[i - 1] - 1
        right_1_cnt = (
            n - not1[j] - 1 if j == len(not1) - 1 else not1[j + 1] - not1[j] - 1
        )

        if left_1_cnt + right_1_cnt >= m - s >= 0:
            ans += (
                min(
                    m - s,
                    left_1_cnt + right_1_cnt - (m - s),
                    left_1_cnt,
                    right_1_cnt,
                )
                + 1
            )
print(ans)
