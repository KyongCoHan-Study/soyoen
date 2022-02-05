# 이항 계수 1

n, k = map(int,input().split())

def fact(n): #팩토리얼
  if n > 0:
    return n * fact(n-1)
  else:
    return 1

# 이항계수 구하는 공식 
print(fact(n) //(fact(k) * fact(n-k)))