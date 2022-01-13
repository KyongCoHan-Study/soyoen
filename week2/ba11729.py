# 하노이탑 이동 순서

def move(start, to):
  print(start, to)

# n개의 원판을 start에서 to로 이동시킨다. via를 통해서
def hanoi(n, start, to, via):
  if n == 1:
    move(start, to)
  else:
    hanoi(n-1, start, via, to) # n-1개를 start에서 via로 이동시킴
    move(start, to) # 맨 마지막 원판을 start에서 to로 이동시킴
    hanoi(n-1, via, to, start) # 나머지 via에 있던 n-1개를 to로 이동시킴

n = int(input())

# 하노이탑 총 이동 횟수
k = 2**n -1

print(k)
hanoi(n, '1', '3', '2')