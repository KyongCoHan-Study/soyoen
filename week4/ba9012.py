# 괄호

t = int(input())

for i in range(t):
  test = input()
  t_count = 0 

  for j in range(len(test)):
    if test[j] == "(":
      t_count += 1
    else:
      t_count -= 1
    if t_count < 0: #올바른 짝이 생기지 않으면 값이 0이하로 떨어짐 -> 올바르지 않은 것
      t_count = 1 #올바르지 않기에 값을 1로 변경하고 
      break #반복문 탈출

  if t_count == 0:
    print('YES')
  else:
    print('NO')