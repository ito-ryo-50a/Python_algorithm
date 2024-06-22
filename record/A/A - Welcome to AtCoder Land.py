# https://atcoder.jp/contests/abc358/tasks/abc358_a


# リファクタリングしたコード(必須)
def check_strings(a, b):
    return "Yes" if a == "AtCoder" and b == "Land" else "No"

def main():
    a, b = input().split()
    result = check_strings(a, b)
    print(result)

if __name__ == "__main__":
    main()


# 解法・記述のポイント



# ACしたコード(必須)
a, b = input().split()
if a=="AtCoder" and b=="Land":
    print("Yes")
else:
    print("No")

