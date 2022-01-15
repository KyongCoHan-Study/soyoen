# 나이순 정렬

import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
  li.append(list(sys.stdin.readline().split()))

li.sort(key=lambda a: (int(a[0])))
# 나이가 동일할 경우 먼저 가입한 순으로 해줘야 하기 때문에 a[1]을 없앴음

for i in range(n):
  print(li[i][0], li[i][1])