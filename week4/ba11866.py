# 요세푸스 문제 0

n, k = map(int,input().split())
num = []
result = []
front = 0
back = n-1
for i in range(n):
  num.append(i + 1)

while back - front != -1:
  for i in range(k-1): # k만큼 앞에 있는 숫자를 뒤로 보냄
    num.append(num[front])
    front += 1
    back += 1
  result.append(num[front]) # k번째마다 저장하고 큐에서 삭제
  front += 1

print("<", end="")
for i in range(n-1):
  print(result[i], end="")
  print(", ", end="")
print(result[n-1], end="")
print(">", end="")