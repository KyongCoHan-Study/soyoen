# 연속합

n = int(input())
array = list(map(int, input().split()))
dp = [0]*n

dp[0] = array[0]

for i in range(1, n):
  dp[i] = max(array[i], dp[i-1] + array[i])
  #dp에 array[i]의 값과 dp[i-1](이전상황 최댓값) + array[i](현재값)중 더 큰 것을 넣음

print(max(dp))
#가장 큰 값을 출력