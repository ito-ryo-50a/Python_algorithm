# https://atcoder.jp/contests/abc359/tasks/abc359_a


# リファクタリングしたコード(必須)
N = int(input())
S = [input() for _ in range(N)]
print(S.count("Takahashi"))


# 解法・記述のポイント
"""
標準入力から値を取得する際に.split()を使用するとデータがlist形式になる
今回は文字列のまま扱う方が良かったため、データ型に注意
"""

# ACしたコード(必須)

N = int(input())
S = [input().split() for _ in range(N)]
ans = 0
i = 0
while i < N:
    if S[i] == ["Takahashi"]:
        ans +=1
        i += 1
    else:
        i += 1
print(ans)

