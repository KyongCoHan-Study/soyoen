# 쿼드트리

n = int(input())
dot = [list(map(int, input())) for _ in range(n)]

def quadTree(x,y,n):
  image = dot[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if image != dot[i][j]: # 0과 1로 압축이 불가능 
        print('(', end='')
        quadTree(x, y, n//2) # 첫번째 분할칸
        quadTree(x, y+n//2, n//2) # 두번째 분할칸
        quadTree(x+n//2, y, n//2) # 세번째 분할칸
        quadTree(x+n//2, y+n//2, n//2) # 네번째 분할칸
        print(')', end='')
        return
  if image == 0:  # 0으로 압축 가능
    print('0', end='')
  else: # 1로 압축 가능
    print('1', end='')

quadTree(0,0,n)