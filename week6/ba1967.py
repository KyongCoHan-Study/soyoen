# 트리의 지름

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input()) #노드의 개수
tree = [ [] for _ in range(n+1)]
for _ in range(n-1):
  a, b, c = map(int, input().split())
  tree[a].append([b,c])
  tree[b].append([a,c])

# 1번 노드에서 가장 먼 곳 찾기
distance = [-1] * (n+1)
distance[1] = 0

def dfs(x, wei): #노드 거리 찾기
  for i in tree[x]:
    a, b = i
    if distance[a] == -1:
      distance[a] = wei + b
      dfs(a, wei+b)

dfs(1,0)

#위에서 찾은 노드에 대한 가장 먼 노드를 찾음
start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))
