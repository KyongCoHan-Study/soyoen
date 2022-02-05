# 배수와 약수

while True:
  t = list(map(int, input().split()))
  if t[0] == 0 and t[1] == 0: #값이 0이면 종료
    break
  if t[1] % t[0] == 0: #약수
    print('factor')
  elif t[0] % t[1] == 0: #배수
    print('multiple')
  else: #아무것도 아님
    print('neither')
