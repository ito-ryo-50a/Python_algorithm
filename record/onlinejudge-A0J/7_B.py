# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_7_B

# リファクタリングしたコード
def count_combinations(n, x):
    ans = sum(
        1 for a in range(1, n + 1)
        for b in range(a + 1, n + 1)
        for c in range(b + 1, n + 1)
        if a + b + c == x
    )
    return ans

for i in range(100):
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    result = count_combinations(n, x)
    print(result)

# 解法のポイント
# 全探索は1行正解できたものをループの中に入れると良い

# ACしたコード

for _ in range(100):
    n, x = map(int, input().split())
    ans = 0
    if n==0 and x==0:
        break
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
          for c in range(b + 1, n + 1):
            if a + b + c == x:
              ans += 1
    print(ans)