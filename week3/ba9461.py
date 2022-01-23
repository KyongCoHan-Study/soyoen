# 파도반 수열

import sys
input = sys.stdin.readline

t = int(input())
arr = [int(input()) for _ in range(t)]
dp = [1,1,1,2,2] #0번째 ~ 5번째까지는 일정하기에 그냥 넣어둠

for i in range(5,max(arr)):
  dp.append(dp[i-2] + dp[i-3]) #i는 i-2번째와 i-3번째를 더한 값과 같음

for i in arr:
  print(dp[i-1])