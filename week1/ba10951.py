# A+B-4

import sys
while True:
  try:
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)
  except:
    break

#예외처리를 해주지 않으면 빠져나올 때 오류가 뜨기 때문에 예외처리 해줄 것