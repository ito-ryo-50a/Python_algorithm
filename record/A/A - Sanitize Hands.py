# https://atcoder.jp/contests/abc357/tasks/abc357_a


# リファクタリングしたコード(必須)
N, M = map(int, input().split())
H = list(map(int, input().split()))
c = 0
s = 0
for h in H:
    if s + h > M:
        break
    s += h
    c += 1
print(c)


# 解法・記述のポイント



# ACしたコード(必須)
N, M = map(int, input().split())
H = [int(a) for a in input().split()]
c = 0
s = 0
while s <= M and c < N:
  s += H[c]
  if s <= M:
    c += 1
print(c)
