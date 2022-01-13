# 블랙잭
import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))
result = 0

for i in range(n-2):
  for j in range(i+1,n-1):
    for k in range(j+1,n):
      save = card[i] + card[j] + card[k]
      if save == m:
        result = save
        break
      elif (save < m) and (save > result):
        result = save
        break

print(result)

# 재귀를 이용하여 풀이 - 참고
'''
def go(n, m, cards, start, cnt, rlt, ans):
    if cnt == 3:
        if rlt <= m:
            ans[0] = max(ans[0], rlt)
        return
    for i in range(start, n):
        go(n, m, cards, i + 1, cnt + 1, rlt + cards[i], ans)


def solution(n, m, cards):
    ans = [0]
    go(n, m, cards, 0, 0, 0, ans)
    return ans[0]


N, M = map(int, input().split())
Cards = list(map(int, input().split()))
print(solution(N, M, Cards))
'''



# 재귀로 해보려다가 망침 ^^
# def process(n, m, card):
#   save = 0
#   first = card[0]
#   second = card[1]
#   third = card[2]
#   for i in range(n):
#     if first + second + third < m:
#       save = first + second + third
#       print('first:',first,'second:',second,'third:',third)
#       print('if 안 save:',save)
#       if i+3 < n:
#         third = card[i+3]
#       else:
#         third = card[i+3]
#         second = card[i+2]
#     elif first + second + third == m:
#       return save

