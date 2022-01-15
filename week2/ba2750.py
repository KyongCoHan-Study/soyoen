# 수 정렬하기

n = int(input())
li = [] # 수를 담을 리스트

for i in range(n):
  x = int(input())
  li.append(x)

li.sort()

print('\n'.join(map(str,li)))


# n = int(input())
# li= []
# for _ in range(n):
#     m = int(input())
#     li.append(m)
# li.sort()

# print(*li)