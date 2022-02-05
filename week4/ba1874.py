# 스택 수열

n = int(input())
stack = []
pp = [] 
count = 1
temp = True

for i in range(n):
  num = int(input())

  while count <= num:
    stack.append(count)
    pp.append('+')
    count += 1
  if stack[-1] == num:
    stack.pop()
    pp.append('-')
  else:
    temp = False
  
if temp == False:
  print('NO')
else:
  for i in pp:
    print(i)