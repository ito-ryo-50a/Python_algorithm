# https://atcoder.jp/contests/abc157/tasks/abc157_b


# リファクタリングしたコード(必須)
A = [list(map(int, input().split())) for _ in range(3)]

M = [[False] * 3 for _ in range(3)]

N = int(input())

for _ in range(N):
    b = int(input())

    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                M[i][j] = True

def check_bingo(M):
    for i in range(3):
        if all(M[i]):
            return True

    for i in range(3):
        if all(M[j][i] for j in range(3)):
            return True

    if all(M[i][i] for i in range(3)) or all(M[i][2 - i] for i in range(3)):
        return True

    return False

if check_bingo(M):
    print("Yes")
else:
    print("No")



# 解法・記述のポイント



# ACしたコード(必須)

A = []
for _ in range(0, 3):
    row = list(map(int, input().split()))
    A.append(row)

M = []
for i in range(0, 3):
    row = []
    for j in range(0, 3):
        row.append(False)
    M.append(row)

N = int(input())

for _ in range(0, N):
    b = int(input())

    for i in range(0, 3):
        for j in range(0, 3):
            if A[i][j] == b:
                M[i][j] = True

bingo = False

for i in range(0, 3):
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

for i in range(0, 3):
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True

if M[0][0] and M[1][1] and M[2][2]:
    bingo = True

if M[0][2] and M[1][1] and M[2][0]:
    bingo = True

if bingo:
    print("Yes")
else:
    print("No")
