# 큐 2

import sys

input = sys.stdin.readline
n = int(input())
queue = []
front = 0 #크기
back = -1

for i in range(n):
  command = input().rstrip()
  if 'push' in command: #push
    queue.append(int(command[5:]))
    back += 1
  elif 'pop' in command: #pop
    if back - front == -1:
      print(-1)
    else:
      print(queue[front])
      front += 1
  elif 'size' in command: #size
    print(back - front + 1)
  elif 'empty' in command: #empty
    if back - front == -1:
      print(1)
    else:
      print(0)
  elif 'front' in command: #front
    if back - front == -1:
      print(-1)
    else:
      print(queue[front])
  elif 'back' in command: #back
    if back - front == -1:
      print(-1)
    else:
      print(queue[back])