# https://atcoder.jp/contests/past202004-open/tasks/past202004_a


# リファクタリングしたコード


# 解法のポイント



# ACしたコード

a, b = input().split()
f = ["B9","B8","B7","B6","B5","B4","B3","B2","B1","1F","2F","3F","4F","5F","6F","7F","8F","9F"]
print(abs((f.index(a))-(f.index(b))))