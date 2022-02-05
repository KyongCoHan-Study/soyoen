# 전깃줄

n = int(input())
line = []
dp = [1]*n

for i in range(n):
  line.append(list(map(int, input().split())))

line.sort() #첫번째 전봇대를 기준으로 오름차순 정렬

for i in range(n):
  for j in range(i):
    if line[i][1] > line[j][1] and dp[i] < dp[j]+1:
      dp[i] = dp[j]+1
    #첫번째 전봇대와 연결되어 있는 두번째 전봇대의 수를 LIS(최장 증가 수열)
    #연결될 수 있는 최대 전깃줄의 수 나옴  

#총 전깃줄 수에서 최대 전깃줄의 수를 빼주면 됨
result = n - max(dp)
print(result)