# https://atcoder.jp/contests/abc359/tasks/abc359_b


# リファクタリングしたコード(必須)
N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(len(A)-2):
    ans += A[i] == A[i+2]

print(ans)


# 解法・記述のポイント
"""
ansはint型
そこに論理演算した結果をインクリメントしたらデータ型の相違で
bool型をint型と算術演算すると
言語仕様で`True`は`1`, `False`は`0`として解釈された上で計算される
"""


# ACしたコード(必須)

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(len(A)-2):
    if A[i] == A[i+2]:
        ans += 1

print(ans)
