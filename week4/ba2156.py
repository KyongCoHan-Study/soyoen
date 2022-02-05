# 포도주 시식

n = int(input())
grape = [] #마심
dp = [0]*n #마시지 않음

for i in range(n):
  grape.append(int(input()))

dp[0] = grape[0] #총 한잔일때
if n > 1: # 총 2잔일 때
  dp[1] = grape[0] + grape[1]
if n > 2: #총 3잔일 때
  dp[2] = max(grape[2] + grape[1], grape[2] + grape[0], dp[1])

for i in range(3,n):
  dp[i] = max(dp[i-1], dp[i-3] + grape[i-1] + grape[i], dp[i-2] + grape[i])
# 현재 포도주를 마시지 않음, 현재와 이전 포도주를 마시고 전전 포도주를 마시지 않음, 현재와 전전포도주를 마시고 이전 포도주를 마시지 않음


print(dp[n-1])