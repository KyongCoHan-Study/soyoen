# 색종이 만들기

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

result = []

def color_paper(x,y,n):
  color = paper[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if color != paper[i][j]:
        color_paper(x, y, n//2) # 첫번째 분할칸
        color_paper(x, y+n//2, n//2) # 두번째 분할칸
        color_paper(x+n//2, y, n//2) # 세번째 분할칸
        color_paper(x+n//2, y+n//2, n//2) # 네번째 분할칸
        return
  if color == 0: #색칠되어 있지 않은 것
    result.append(0)
  else: #색칠되어 있는 것
    result.append(1)

color_paper(0,0,n)

print(result.count(0))
print(result.count(1))