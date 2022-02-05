# 프로그래머스 - 그리디 - 조이스틱

def solution(name):
  alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  al_reverse = list(reversed(alpha))
  cnt = 0
  min_move = len(name) - 1 # 한 방향으로만 이동했을 때
  next = 0

  for i in name:
    print('--',i,'--')
    if i in alpha[:13]:
      print(alpha.index(i))
      cnt += alpha.index(i)
    else:
      print(al_reverse.index(i)+1)
      cnt += al_reverse.index(i)+1 

  while name[min_move] == 'A' and min_move > 0:
    min_move -= 1
    
  if (min_move < 0):
    return cnt

  for i in range(len(name)):
    next = i + 1
    while next < len(name) and name[next] == 'A':
      next += 1
    min_move = min(min_move, i+(i + len(name)) - next )

  answer = cnt + min_move
  return answer

# 74.1%에서 올릴 수 없음...ㅜ
  
solution('JAN')


  # for j in name:
  #   if len(name_li) -1 == name_li.count('A'):
  #     cnt += len(name) -1 - name_li.count('A')
  #     break
  #   elif len(name_li) == name_li.count('A'):
  #     break
  #   else:
  #     cnt += 1
  #     name_li.remove(j)

# https://bellog.tistory.com/152