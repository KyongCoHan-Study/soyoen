# 별 찍기 - 2

# n = int(input())

# for i in range(1,n+1):
#   print(' '*(n-i)+'*'*i)

'''
for i in range(1,t+1):
  print(('*'*i).rjust(t))

zfill() = 기존 문자열 왼쪽에 0을 채워줌. 문자열의 형태만 가능함
n = str(5)
n.zfill(3) -> 005

rjust() = 기존 문자열은 오른쪽 정렬이 되며, 원하는 문자열을 기존 문자열의 왼쪽에 채워줌.
n.rjust(3,x) -> xx5
n.rjust(4) -> ,,,5 (이때 , 은 공백을 의미)

ljust() = 기존 문자열을 왼쪽 정렬, 원하는 문자열을 오른쪽에 채움
n.ljust(3,x) -> 5xx
n.ljust(4) -> 5,,, (이때 , 은 공백을 의미)

'''
n = str(5)
print(n.ljust(4))