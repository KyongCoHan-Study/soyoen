# 주유소
import sys

n = int(sys.stdin.readline())
road = list(map(int,sys.stdin.readline().split()))
oil = list(map(int,sys.stdin.readline().split()))
result = 0 # 결과 출력할 값
min_oil = oil[0] # 최소 기름값에 0번째 리스트 넣음

for i in range(n-1):
  if oil[i] < min_oil: #만약 i번째가 최소값보다 작다면
    min_oil = oil[i] # min_oil을 i번째 값으로 바꾸기
  result += min_oil * road[i] # 최소기름 값과 거리를 계산해서 결과 출력
print(result)


''' 17점 나온 답
# min_oil = min(oil[:3]) 가장 기름값이 적은 것 찾기
all_road = 0 # 총 가야하는 거리 구하기
for i in road:
  all_road += i

for i in range(n-1): #마지막 기름은 필요없기에 반복 돌지 않음
  if oil[i] == min(oil[:3]): #기름값이 가장 적다면
    result += oil[i] * all_road # 그 곳에서 남은 거리의 기름을 다 구매
    break #그리고 반복 중지
  else: # 아니라면 최소한의 기름을 구매
    result += road[i] * oil[i]
    all_road -= road[i]
print(result)
'''