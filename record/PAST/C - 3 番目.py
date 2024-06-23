# https://atcoder.jp/contests/past201912-open/tasks/past201912_c


# リファクタリングしたコード



# 解法のポイント
a = list(map(int, input().split()))
a.sort(reverse=True)
print(a[2])


# ACしたコード
a = list(map(int, input().split()))
a.sort()
print(a[3])