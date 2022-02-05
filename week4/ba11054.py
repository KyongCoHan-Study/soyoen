# 가장 긴 바이토닉 부분 수열

a = int(input())
array = list(map(int,input().split()))
reverse_array = array[::-1]
in_dp = [1 for i in range(a)] 
#가장 긴 증가하는 부분 수열의 길이
de_dp = [1 for i in range(a)]
#가장 긴 감소하는 부분 수열의 길이

for i in range(a): #현재 위치
  for j in range(i): #이전 위치
    if array[i] > array[j]:
      in_dp[i] = max(in_dp[i], in_dp[j]+1) #현재와 이전 위치 중 최댓값 구하고 해당 길이에 +1
    if reverse_array[i] > reverse_array[j]:
      de_dp[i] = max(de_dp[i], de_dp[j]+1)

result = [0 for i in range(a)]
for i in range(a):
  result[i] = in_dp[i] + de_dp[a-i-1] -1
  #de_dp[a-i-1]인 이유, 기존 array를 뒤집어서 구했기 때문에 
  #in_dp와 맞는 순서로 해주기 위해서 끝에서 부터 꺼내서 더해줌. 그래서 a-i-1을 함
  #마지막 -1은 가장 큰 수가 중복되었기에 길이에서 1을 뺌
print(max(result))