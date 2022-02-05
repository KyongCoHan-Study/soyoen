# 평범한 배낭

n, k = map(int,input().split())
bag = [[0] * (k+1) for i in range(n+1)]
item = [[0,0]]

for i in range(n):
  item.append(list(map(int,input().split())))

for i in range(1, n+1):
  for j in range(1, k+1):
    w = item[i][0]
    v = item[i][1]
    if j < w: #현재 가방 무게가 아이템 무게보다 가볍다면
      bag[i][j] = bag[i-1][j]
    else:
      bag[i][j] = max(bag[i-1][j], bag[i-1][j-w]+v)
      # max(bag[이전물건][현재가방무게], bag[이전물건][현재가방무게-현재물건무게]+현재물건가치)

print(bag[n][k])