# 트리의 지름

from collections import deque
import random

v = int(input()) #노드의 개수
tree = [ [] for _ in range(v+1) ]

#정점 번호, 간선정보(정점번호, 거리, 마지막 입력 -1)
for _ in range(v):
  #0번째는 정점번호
  node = list(map(int, input().split()))
  for i in range(1, len(node) -2, 2):
    #1~len(node)의 길이 -2번째 (정점번호, 거리, 정점번호, 거리) 순으로 데이터 저장
    cur_edge = node[0] #0번째는 정점번호
    edge, cost = node[i],  node[i + 1] #연결되 노드와 거리 (정점번호, 거리)
    tree[cur_edge].append((edge, cost))

def bfs(start):
  #-1 은 마지막 인덱스
  visit = [-1] * (v+1)
  q = deque()
  q.append(start)
  visit[start] = 0
  #거리가 가장 먼 트리의 지름과 정점을 저장하는 배열
  max = [0, 0]

  while q:
    # 현재 기준 노드
    x = q.popleft()
    #현재 기준 노드 x와 연결된 노드 중에서 거리가 가장 먼 노드를 찾는 과정
    for e, d in tree[x]:
      #연결된 노드 중 아직 방문하지 않은 노드의 거리 갱신
      if visit[e] == -1:
        visit[e] = visit[x] + d
        q.append(e)
        #현재 노드로부터 거리가 가장 먼 노드의 번호와 거리 갱신
        if max[0] < visit[e]:
          max = visit[e], e
  return max

# 트리에서 임의의 노드 x를 설정
random_node = random.randrange(1, v+1)
# 노드 x를 기준으로 가장 먼 노드 y를 탐색
distance, node = bfs(random_node)
# 노드 y를 기준으로 가장 먼 노드 z를 탐색
distance, node = bfs(node)
# 트리의 지름: 노드 y와 노드 z 사이의 거리
print(distance)

