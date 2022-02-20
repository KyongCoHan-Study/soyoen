# 단지번호붙이기

n = int(input())
graph = []
answer = []
dx = [0,0,1,-1] # 동서남북 인접한 곳의 좌표를 구하기 위함
dy = [1,-1,0,0]
cnt = 0

for i in range(n):
  x = list(map(int, input()))
  graph.append(x)

def dfs(x,y):
  global cnt
  graph[x][y] = '#'
  cnt += 1 #탐색을 시작할 때마다 카운트
  for k in range(4): #동서남북 인접한 네 방향에 대해서
    nx = x + dx[k]
    ny = y + dy[k]
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
      #인전합 곳의 좌표가 범위 내이고, 1이리면
      graph[nx][ny] = '#' #방문한 곳으로 처리
      dfs(nx, ny) #조건을 만족하는 지점에서 다시 탐색
  return cnt

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      cnt = 0
      answer.append(dfs(i, j))

print(len(answer))
answer.sort()

for i in answer:
  print(i)