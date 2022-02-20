# 두 수의 합

n = int(input()) #수열의 크기
li = list(map(int,input().split())) 
x = int(input()) #자연수 x

count = 0
li.sort()

start, end = 0, n-1 #투 포인터 

while start != end: #시작과 끝이 같을 때 반복
  if li[start] + li[end] == x: #시작과 끝의 합이 같으면 카운트, 시작 1 증가
    count += 1
    start += 1

  elif li[start] + li[end] > x: # 더 크면 끝 1 감소
    end -= 1

  else: #더 작으면 시작 1 증가
    start += 1

print(count)
