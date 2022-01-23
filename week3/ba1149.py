# RGB거리

import sys
input = sys.stdin.readline

n = int(input())
money = []
for i in range(n):
  money.append(list(map(int,input().split())))

# 현재 집에서 각각 색을 칠했을 때의 가장 적은 비용을 저장해서 재사용해야 함
for i in range(1,len(money)):
  #0,1,2 == 빨강 초록 파랑
  money[i][0] += min(money[i-1][1], money[i-1][2])
  money[i][1] += min(money[i-1][0], money[i-1][2])
  money[i][2] += min(money[i-1][0], money[i-1][1])
  # 이전 집(i-1)에 색칠했을 때의 최솟값을 가지고 옴
  # 현재 색을 제외하고 나머지 두개의 색 비용중 최솟값을 가져 옴
  # 이러면 각 색을 칠했을 때의 최솟값이 배열로 저장됨

# 마지막 열이 최종적으로 얻을 수 있는 최솟값이 됨
# 마지막 열에 있는 0,1,2번째 값들 중 가장 작은 값을 뽑아냄
print(min(money[-1]))
# money[-1] = money[n-1][0],money[n-1][1],money[n-1][2]