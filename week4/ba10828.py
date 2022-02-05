# 스택

import sys

input = sys.stdin.readline
n = int(input())
stack = []

for i in range(n):
  command = input().rstrip()
  if 'push' in command: #push
    stack.append(int(command[5:]))
  elif 'pop' in command: #pop
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())
  elif 'size' in command: #size
    print(len(stack))
  elif 'empty' in command: #empty
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif 'top' in command: #top
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[len(stack)-1])