# 숫자 카드 2

import sys

input = sys.stdin.readline

n = int(input())
nlist = sorted(map(int, input().split())) #이분탐색을 위해 정렬
m = int(input())
mlist = map(int, input().split())

def binary_search(N, nlist, start, end):
  if start > end: #nlist의 요소인 N을 중간값과 비교
    return 0
  M = (start+end)//2
  if N == nlist[M]: #N이 중간요소인 경우 
    return nlist[start:end+1].count(N) #start에서 end까지의 범위에서 count로 몇개 있는지 카운트
  elif N < nlist[M]: #N이 중간요소가 아닌 경우 중 N이 nlist[M]보다 작을 때
    return binary_search(N, nlist, start, M-1) #탐색 범위를 절반으로 나눈 후 이분 탐색을 진행
  else: #N이 중간요소가 아닌 경우 중 N이 nlist[M]보다 클 때
    return binary_search(N, nlist, M+1, end)

n_dic = {} #리스트 nlist에 있는 요소들이 각각 몇개가 있는지 저장
for N in nlist:
  start = 0
  end = len(nlist) -1
  if N not in n_dic: 
    n_dic[N] = binary_search(N, nlist, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in mlist))