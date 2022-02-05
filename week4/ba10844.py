# 쉬운 계단 수

n = int(input())

dp = [[0]*10 for _ in range(n+1)]
for i in range(1,10):
  dp[1][i] = 1

for i in range(2, n+1):
  for j in range(10):
    if j == 0:
      dp[i][j] = dp[i-1][1] #0개, 0으로 시작은 세지 않음
    elif j == 9:
      dp[i][j] = dp[i-1][8] #1개, 9는 8밖에 없음
    else:
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] #2개

result = sum(dp[n]) % 1000000000 #sum으로 저장된 것들을 모두 더함
print(result)