# https://atcoder.jp/contests/past202004-open/tasks/past202004_b


# リファクタリングしたコード
arr = input()
counts = {'a': arr.count('a'), 'b': arr.count('b'), 'c': arr.count('c')}
max_char = max(counts, key=counts.get)
print(max_char)


# 解法のポイント
S = input()
na = S.count("a")
nb = S.count("b")
nc = S.count("c")
mx = max(na, nb, nc)
if na == mx:
    print("a")
elif nb == mx:
    print("b")
elif nc == mx:
    print("c")


# ACしたコード
arr = input()
a = arr.count("a")
b = arr.count("b")
c = arr.count("c")
if a > b and a > c:
    print("a")
elif b > a and b > c:
    print("b")
elif c > a and c > b:
    print("c")