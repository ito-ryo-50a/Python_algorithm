# https://atcoder.jp/contests/abc357/tasks/abc357_b


# リファクタリングしたコード(必須)
S = input()
up = sum(1 for c in S if c.isupper())
lo = sum(1 for c in S if c.islower())
print(S.upper() if up > lo else S.lower())



# 解法・記述のポイント



# ACしたコード(必須)
S = input()
up = sum(map(str.isupper, S))
lo = sum(map(str.islower, S))

if up > lo :
    print(S.upper())
else:
    print(S.lower())

