# 신나는 함수 실행

import sys

# 3중 리스트를 만들어 값을 지정할 수 있게 함. 범위는 2-을 넘어가게 되면 다 20으로 만듦
# 그래서 인덱스를 0~20까지 쓸 수 있도록 함
dp = [[[0 for _ in range(21)] for _ in range (21)] for _ in range (21)]

def w(a,b,c):
  # 0보다 작으면 1로 리턴
  if a <= 0 or b <= 0 or c <= 0:
    return 1
  elif a > 20 or b > 20 or c > 20:
    return w(20, 20, 20)

  if dp[a][b][c]:
    return dp[a][b][c]

  if a < b < c:
    dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
  else:
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

  return dp[a][b][c]

while True:
  a,b,c, = map(int,sys.stdin.readline().split())
  if a == -1 and b == -1 and c == -1:
    break
  print(f'w({a}, {b}, {c}) = {w(a,b,c)}')

''' key로 푸는 문제
import sys
read = sys.stdin.readline

cache = {}

def w(a, b, c):
  if a <= 0 or b <= 0 or c <= 0:
      return 1
  if a > 20 or b > 20 or c > 20:
      return w(20, 20, 20)
      
  key = '{} {} {}'.format(a, b, c)
  
  ### 핵심코드 ### 주어진 W함수에서 중간에 계산된 값을 지정하고 재사용할 수 있는 분기
  if key in cache:
      return cache[key]
  res = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
  cache[key] = res
  값을 저장하기 위한 cache를 딕셔너리 형태로 선언하고 a,b,c를 이용하여 string형태로 만들어 key값으로 사용
  ################
  
  return res

while True:
  a,b,c = map(int, read().split())
  if a == -1 and b == -1 and c == -1:
      break
  print('w({}, {}, {}) = {}'.format(a, b, c, w(a, b, c)))
'''