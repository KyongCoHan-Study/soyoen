# DFS와 BFS

from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().strip().split())
edge = [[] for i in range(n+1)]

for i in range(m):
  v1, v2 = map(int, input().strip().split())
  edge[v1].append(v2)
  edge[v2].append(v1)

for i in edge:
  i.sort()

d_check = [False for i in range(n+1)]
def dfs(x):
  d_check[x] = True
  print(x, end=' ')
  for y in edge[x]:
    if d_check[y] == False:
      dfs(y)

def bfs():
  queue = deque([v])
  b_check = [False for i in range(n+1)]
  b_check[v] = True
  while queue:
    b = queue.popleft()
    print(b, end=' ')
    for i in edge[b]:
      if not b_check[i]:
        b_check[i] = True
        queue.append(i)

dfs(v)
print()
bfs()
print()