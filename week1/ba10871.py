# X보다 작은 수

import sys
n, x = map(int, sys.stdin.readline().split())
a = list(sys.stdin.readline().split())

for i in range(n):
  if x > int(a[i]):
    print(int(a[i]))