# 바이러스

n = int(input()) #컴퓨터 수
m = int(input()) #연결된 컴퓨터 쌍의 수
graph = [[] for i in range(n+1)] #인접리스트 선언 및 입력받기

for i in range(m): #연결된 컴퓨터 쌍의 수만큼 반복
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visite = [0] * (n+1) #방문처리: 방문한 컴퓨터 수를 출력해야 함
#visite에 True/False가 아닌 0/1로 처리
def dfs(graph, v, vistie):
  visite[v] = 1
  for i in graph[v]:
    if visite[i] == 0:
      dfs(graph, i, visite)
  return True

dfs(graph, 1, visite)
print(sum(visite)-1) #방문한 컴퓨터 개수 - 1번 컴퓨터 