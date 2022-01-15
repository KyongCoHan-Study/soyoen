# 좌표 정렬하기 2
import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
  # li.append(input().split())
  li.append(list(map(int,sys.stdin.readline().split())))

li.sort(key=lambda a: (a[1],a[0])) # 원하는 인덱스로 정렬함
# key값에 무명함수를 사용하여 1번째 인덱스로 정렬하게 함

print('---- 정렬 후 ----')
for i in range(n):
  print(li[i][0], li[i][1])

# 틀렸다고 나오는데 왜 틀렸다는지 모루겠음

#이중 리스트를 벗길 수는 없었다...
# print('\n'.join(map(str,li)))