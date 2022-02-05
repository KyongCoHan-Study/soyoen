# 다리 놓기

t = int(input())

for i in range(t):
  n,m = map(int, input().split())
  N = n
  M = m
  while n != 1:
    n -= 1
    N *= n
    m -= 1
    M *= m
  print(M//N)

#11050방식으로는 불가 -> 이유: 범위가 커져 재귀를 통해 해결불가
#재귀의 깊이가 너무 깊어서 컴파일에 실패하기 때문