# 연산자 끼워넣기
import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
add, sub, mul, div = map(int,sys.stdin.readline().split()) # 연산자의 갯수
max_result = -1000000001
min_result = 1000000001

def dfs(x,med):
  global add, sub, mul, div, max_result, min_result

  if x == n:
    max_result = max(max_result, med) #계산한 값과 결과값에 들어간 값중 가장 큰것을 최종 최대값으로 함
    min_result = min(min_result, med)
  else:
    if add > 0: #더하기 연산자가 1개이상 있다면
      add -= 1 #더하기 연산자 갯수 차감
      dfs(x + 1, med + a[x]) #더하기 계산
      add += 1 #추후 다른 연산을 위해 다시 추가
    if sub > 0:
      sub -= 1
      dfs(x + 1, med - a[x])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(x + 1, med * a[x])
      mul += 1
    if div > 0:
      div -= 1
      dfs(x + 1, int(med / a[x]))
      div += 1

dfs(1,a[0]) #계산한 수, 연산 시작 값
print(max_result)
print(min_result)