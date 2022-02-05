# 검문

n = int(input())
num = []
for i in range(n):
  num.append(int(input()))
num.sort()

def euclidean(a,b): #유클리드 호제법
  if b == 0:
    return a
  else:
    return euclidean(b, a%b)

max_fac = num[1] - num[0] #붙어있는 항 끼리 차를 구함
for i in range(1, n-1):
  max_fac = euclidean(num[i+1]-num[i], max_fac) #모든 차에 대한 최대공약수 

m = [max_fac]
for i in range(2, int(max_fac ** 0.5)+1):
  if max_fac % i == 0:
    m.append(i)
    if i != max_fac // i:
      m.append(max_fac // i)

m.sort()
for i in m:
  print(i, end=' ')

#참고 글
#https://moz1e.tistory.com/40 

''' 값은 제대로 나오지만 실패라고 뜬다 (범위때문에 그런 듯)
n = int(input())
li = []
m = []

for i in range(n):
  li.append(int(input()))

# 첫 for문의 범위를 어떻게 정해야 할지 모르겠어서 실패..
for i in range(2,n+2):
  t = []
  # print('i:',i)
  for j in range(n):
    # print('li[j]:',li[j])
    if li[j] % i == 0:
      t.append(0)
    elif li[j] % i == 1:
      t.append(1)
    elif li[j] % i == 2:
      t.append(2)
  # print(t)
  if t.count(0) == n:
    m.append(str(i))
  elif t.count(1) == n:
    m.append(str(i))
  elif t.count(2) == n:
    m.append(str(i))
  # print(m)

print(" ".join(m))
'''