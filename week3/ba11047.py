# 동전 0

import sys
n, k = map(int,sys.stdin.readline().split())
coin = []
cnt = 0

for i in range(n):
  coin.append(int(sys.stdin.readline()))
coin = reversed(coin)
for i in coin:
  if i <= k:
    cnt += k // i
    k %= i
print(cnt)