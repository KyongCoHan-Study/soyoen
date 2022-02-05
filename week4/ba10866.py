# 덱

import sys
input = sys.stdin.readline

n = int(input())
deque = []

for i in range(n):
  command = input().rstrip()
  if 'push_front' in command: #push_front
    deque.insert(0, int(command[11:]))
  elif 'push_back' in command: #push_back
    deque.append(int(command[10:]))
  elif 'pop_front' in command: #pop_front
    if len(deque) == 0:
      print(-1)
    else:
      print(deque[0])
      deque.pop(0)
  elif 'pop_back' in command: #pop_back
    if len(deque) == 0:
      print(-1)
    else:
      print(deque[len(deque)-1])
      deque.pop()
  elif 'size' in command: #size
    print(len(deque))
  elif 'empty' in command: #empty
    if len(deque) == 0:
      print(1)
    else:
      print(0)
  elif 'front' in command: #front
    if len(deque) == 0:
      print(-1)
    else:
      print(deque[0])
  elif 'back' in command: #back
    if len(deque) == 0:
      print(-1)
    else:
      print(deque[len(deque)-1])