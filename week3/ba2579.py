# 계단 오르기

import sys

input = sys.stdin.readline
n = int(input())
arr = [] #입력받을 배열
dp = [] #dp에 사용될 배열

# 계단에 쓰여진 점수 저장
for _ in range(n):
  arr.append(int(input()))

#계단이 1,2개일 때의 경우를 해주지 않으면 인덱스 오류 뜸
#밑에 하드코딩 3개는 무조건 돌아가는데 계단이 1개라면 1,2인덱스가 없기 때문에 오류가 남
if n == 1: #계단이 하나일 때
  print(arr[0]) 
  exit() 
elif n == 2: #계단이 2개 일때
  print(max(arr[0]+arr[1], arr[1])) 
  exit()

#dp에 앞에서부터 밟아온 계단 중 가장 최대의 값을 저장
# dp[4] => 네번째 계단까지 계산했을 때 가장 큰 경우의 값
dp.append(arr[0])
dp.append(max(arr[0]+arr[1],arr[1])) 
dp.append(max(arr[0]+arr[2],arr[1]+arr[2])) 
# 위의 3코드를 for문에 넣지 않은 것은 i-3때문. 인덱스 범위를 넘어가지 않게 하기 위해서
for i in range(3,n): 
  dp.append(max(dp[i-2] + arr[i] , dp[i-3] + arr[i] + arr[i - 1])) 
  # 마지막 칸을 밟기 전 
  # 밟은 계단이 끝에서 두번째(i-2)인 경우, i-2계단 까지의 최대 가중치 합 + 현재 계단의 가중치
  # 밟은 계단이 끝에서 첫번째(i-1)일 경우, 끝에서 두번째(i-2) 계단은 밟으면 안됨
  # 그래서, i-3번째 계단까지의 최대 가중치 합 + i-1번째 계단의 가중치 + 현재 계단의 가중치
  # 중에서 더 큰 값을 넣음

print(dp.pop()) #뽑아내고 비움