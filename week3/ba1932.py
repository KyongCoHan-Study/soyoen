# 정수 삼각형

import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
  arr.append(list(map(int,input().split())))

for i in range(1,n):
  for j in range(i+1):
    if j == 0:
      arr[i][j] = arr[i][j] + arr[i-1][j]
    elif j == i:
      arr[i][j] = arr[i][j] + arr[i-1][j-1]
    else:
      arr[i][j] = max(arr[i-1][j-1], arr[i-1][j]) + arr[i][j]

# 마지막 열에서 가장 큰 값을 골라서 출력하면 최대값이 나옴
print(max(arr[n-1]))