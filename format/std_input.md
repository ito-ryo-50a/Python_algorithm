### 入力内容
```
abc
```
##### 記述するコード
```
a = input()
```
##### 変数に代入される中身
```
a: "abc"
```


### 入力内容
```
100
```
##### 記述するコード
```
a = int(input())
```
##### 変数に代入される中身
```
a: 100
```


### 入力内容
```
5
abcde
```
##### 記述するコード
```
a = int(input())
b = input()
```
##### 変数に代入される中身
```
a: 5
b: "abcde"
```


### 入力内容
```
5
1 2 3 4 5
```
##### 記述するコード
```
n = int(input())
a = list(map(int, input().split()))
```
##### 変数に代入される中身
```
n: 5
a: [1, 2, 3, 4, 5]
```


### 入力内容
```
100 10
```
##### 記述するコード
```
n, m = list(map(int, input().split()))
```
##### 変数に代入される中身
```
n: 100
m: 10
```


### 入力内容
```
```
##### 記述するコード
```
a = input().split()
```
##### 変数に代入される中身
```
a: ""
```


### 入力内容
```
```
##### 記述するコード
```
N = int(input())
A = [input().split() for _ in range(N)]
```
##### 変数に代入される中身
```
A: 
```



### 入力内容
```
```
##### 記述するコード
```
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
```
##### 変数に代入される中身
```
A: 
```
