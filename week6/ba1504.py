# 특정한 최단 경로

import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
  res = [float('INF') for _ in range(V)]
  res[start] = 0
  q = []
  heapq.heappush(q, (res[start], start))
  while q:
    result_x, x = heapq.heappop(q)
    for fu, fw in graph[x]:
      if res[fu] > result_x + fw:
        res[fu] = result_x + fw
        heapq.heappush(q, ([res[fu], fu]))
  return res

V, E = map(int,input().split())
graph = [[] for _ in range(V)]
for _ in range(E):
  u, v, w = map(int,input().split())
  graph[u-1].append((v-1, w))
  graph[v-1].append((u-1, w))
v1, v2 = map(int,input().split())

# 1번 -> N번 정점 경우의 수: 1 -> v1 -> v2 -> N  /  1 -> v2 -> v1 -> N
ans = dijkstra(0)
dv1 = dijkstra(v1-1)
dv2 = dijkstra(v2-1)
dab = min(ans[v1-1] + dv1[v2-1] + dv2[V-1], ans[v2-1] + dv2[v1-1] + dv1[V-1])
print(-1) if dab == float('inf') else print(dab)