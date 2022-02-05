#가장 긴 증가하는 부분 수열

a = int(input())
array = list(map(int,input().split()))
dp = [1 for i in range(a)] 
#array[i]를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 길이

for i in range(a): #현재 위치
  for j in range(i): #이전 위치
    if array[i] > array[j]:
      dp[i] = max(dp[i], dp[j]+1) #현재와 이전 위치 중 최댓값 구하고 해당 길이에 +1

print(max(dp)) #dp원소 중 가장 큰 원소 출력