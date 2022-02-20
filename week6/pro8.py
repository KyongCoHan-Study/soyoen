# 프로그래머스 - 깊이/너비 우선 탐색 (dfs,bfs) - 타겟넘버

def solution(numbers, target):
  total = [0] #전체 노드의 합을 더해줄 리스트
  for i in numbers:
    sub = [] #각 단계를 수행하고 나서 계산된 값 저장
    for j in total: #total의 원소만큼 반복 => +,-인 경우에 대해 반복
      sub.append(j+i)
      sub.append(j-i)
    total = sub #sub에서 계산한 값을 total에 저장
  return total.count(target) #target과 일치하는 원소의 개수를 count