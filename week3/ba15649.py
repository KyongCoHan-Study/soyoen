# N과 M (1)

import sys
n, m = map(int,sys.stdin.readline().split())
vis = [] #출력할 것을 담은 리스트

def backtracing():
  if len(vis) == m: #리스트에 담긴 것의 수가 m개와 같다면
    return print(' '.join(map(str,vis))) #리스트에 담긴 것 출력
  for i in range(1,n+1): #1부터 n+1개까지 반복
    if i not in vis: #만약에 출력리스트에 i가 없다면
      vis.append(i) #i를 리스트에 추가
      backtracing() #해당 함수를 또 실행 ex) 현재 i =1 함수 또 실행 그럼 그 함수 안에서 i = 1,2,3...이 됨
      vis.pop() #위에 함수 실행으로 길이가 리스트에 길이가 채워져 출력되었으니 리스트를 다시 비워줌

backtracing()