# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_7_B

# リファクタリングしたコード
for _ in range(100):
    n, x = map(int, input().split())
    ans = 0
    if n==0 and x==0:
        break
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            c = (x - a - b)
            if not a < b < c:
                continue
            if 1 <= c <= n:
                ans += 1
    print(ans)

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