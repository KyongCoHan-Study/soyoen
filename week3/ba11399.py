# ATM
import sys

n = int(sys.stdin.readline())
p = list(map(int,sys.stdin.readline().split()))
result = 0 # 최종 결과 값
save = 0 # 앞 시간들을 저장할 값

p.sort() # 최소의 수를 만들기 위해 정렬(오름차순)

for i in range(n):
  if i == 0: # 0번째 리스트는 가장 먼저 시작하기에 그냥 저장
    save += p[i]
    result += save
  else: #1번째 리스트부터 앞의 시간을 더해줘야 함
    save += p[i] #현재의 값을 앞 시간의 값과 더해줌
    result += save # 결과값에 추가

print(result)