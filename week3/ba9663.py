# N-Queen

# python은 안되고 pypy로 제출할 것
n, ans = int(input()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)
# a는 세로 줄 확인, b는 /대각선 줄, c는 \대각선 줄
def solve(i):
  # i 는 행
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n): # j는 열
        if not (a[j] or b[i+j] or c[i-j+n-1]):
          #a[j]는 세로 줄 확인  b[i+j]는 /대각선 확인 c[i-j+n-1]는 \대각선 확인
          #[]안에 값들은 현재 위치에서 세로,/,\줄들의 값이 무엇이 있는지 구하는 식 
            a[j] = b[i+j] = c[i-j+n-1] = True
            solve(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

solve(0)
print(ans)


#출처: https://rebas.kr/761 [PROJECT REBAS]

'''시간초과
import sys
n = int(sys.stdin.readline())
res = 0
col = [0] * 15

def check(x):
  for i in range(x):
    if col[x] == col[i] or abs(col[i]-col[x]) == x-i:
      return False
  return True

def dfs(x):
  global res
  if x == n:
    res += 1
    return
  for i in range(n):
    col[x] = i
    if check(x):
      dfs(x+1)
dfs(0)
print(res)

'''


''' 시간초과
import sys
n = int(sys.stdin.readline())
count = 0
graph = [0 for _ in range(n + 1)]

# 모든 퀸은 한 행에 한개씩 들어가기 때문에 행검사는 할 필요 없다
# 열 검사와 대각 검사만 하면 됨
# 위에서부터 차례로 내려오기 때문에 해당 row 전까지만 검사하면 된다

# 백트래킹을 위한 검사 함수
# col에는 가능한 col후보가 들어감
def promising(graph, row, col):
    # 열 검사
    for i in range(1, row): #이전 행에서 현재 행까지 점유되었는지만 검사하면 된다.
        if graph[i] == col: #현재 검사하려는 열이 점유되었는지 검사한다.
            return False    #위협받는 위치라면 False 반환하고 함수 종료
    # 대각 검사
    for i in range(1, row):
        if abs(graph[i] - col) == row - i:
            return False
    return True #위 검사를 모두 통과하면 True 반환

def nqueen(graph, row, num):
    global count

    if row == num + 1:                  #N개의 행을 모두 검사하면 재귀 종료
        count += 1
        return

    # 1 ~ n 까지의 col 후보 중 가능 한 후보를 판별
    for col in range(1, n + 1):
        if promising(graph, row, col):  #위치 검사를 통과하면
            graph[row] = col            #해당 행에 열 정보를 입력하고
            nqueen(graph, row + 1, num) #다음 행 검사를 시작
        else:
            continue                    #위치검사를 통과하지 못하면 다음 열 검사
            
            # 해당 행의 모든 열 검사가 종료되면 함수 종료

nqueen(graph, 1, n)
print(count)
'''