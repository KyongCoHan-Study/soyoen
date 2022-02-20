# 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
tree = [ [] for _ in range(n+1) ]
parent = [ 0 for _ in range(n+1)]
for _ in range(n-1):
  i, j = map(int, input().split())
  tree[i].append(j)
  tree[j].append(i)

def dfs(start, tree, parent):
  for i in tree[start]: #연결된 노드 모두 탐색
    if parent[i] == 0: #방문한 적이 없다면
      parent[i] = start #부모노드 저장
      dfs(i, tree, parent)

dfs(1, tree, parent)

for i in range(2, n+1):
  print(parent[i])