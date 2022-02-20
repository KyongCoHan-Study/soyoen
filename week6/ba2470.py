# 두 용액

import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()

start, end = 0, n-1 #투 포인터 
sum = 9999999999999
one = 0
two = 0

while start < end:
  total = li[start] + li[end]
  zero = abs(total)

  if sum > zero:
    sum = zero
    one = li[start]
    two = li[end]

  if total > 0: 
    end -= 1

  else: 
    start += 1

print(one, two)