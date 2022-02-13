# 종이의 개수

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

minus = 0
plus = 0
zero = 0

def count_paper(x,y,n):
  global minus, plus, zero

  num = board[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if board[i][j] != num:
        for k in range(3):
          for l in range(3):
            count_paper(x+k*n//3, y+l*n//3, n//3)
        return
  if num == -1:
    minus += 1
  elif num == 1:
    plus += 1
  else:
    zero += 1

count_paper(0,0,n)

print(minus)
print(zero)
print(plus)