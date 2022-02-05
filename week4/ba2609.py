# 최대공약수와 최소공배수

A,B = map(int, input().split())
a,b = A,B

#유클리드 호제법: a와 b의 쵀대공약수 G는 b와 a%b의 최대공약수 G'와 같다
# 그래서 b가 0이 되는 순간의 a가 최대공약수
while b!= 0:
  a = a % b #a는 나머지 값이 됨
  a,b = b,a 
print(a) #최대공약수
print(A*B//a) #최소공배수 


''' 시간초과로 실패 ㅎ;
def factorization(n):
  factor = []
  while n != 1:
    for i in range(1, n+1):
      if n % i == 0:
        factor.append(i)
        factor.append(n // i)
        break
  return factor

a_fac = factorization(a)
b_fac = factorization(b)
a_fac = set(a_fac)
b_fac = set(b_fac)
a_fac.sort()
b_fac.sort()
max_fac = 1

for i in range(len(a_fac)):
  for j in range(len(b_fac)):
    if a_fac[i] == b_fac[j]:
      max_fac *= a_fac[i]
      print(max_fac)
      a_fac[i] == 0
      b_fac[j] == 0

min_mul = max_fac * (a // max_fac) * (b // max_fac)
print(max_fac)
print(min_mul)
'''
