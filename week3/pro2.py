# 프로그래머스 - 완전탐색 - 소수 찾기

from itertools import permutations

#소수 판별 함수
def is_prime_number(x):
  if x < 2: # 1은 포함을 안 할 것이기 때문에
    return False
  
  for i in range(2,x):
    if x % i == 0: #나누어 떨어지면 소수가 아님
      return False
  return True

def solution(numbers):
  answer = 0
  num = []

  for i in range(1,len(numbers) +1):
    # list로 만들고 set을 통해 중복 확인, join으로 연결, permutations로 iterable(numbers)의 요소들의 길이가 i인 순열로 반환
    num.append(list(set(map(''.join, permutations(numbers, i)))))
    # 결과 [['1'].['7'].['71'],['17']]
  per = list(set(map(int,set(sum(num, [])))))
  #위의 이중리스트를 1차원으로 바꾸기 위해 sum사용
  # sum(덧셈할 것, 처음에 더할 것) -> 처음에 더할 것을 빈 리스트로 넣어줌
  # sum(num,[]) => [] + [1,7] + [71,17] 이 되어 리스트끼리의 덧셈으로 [1,7,71,17]이 됨.
  # 혹시 이때 중복이 있을 수 있기에 set사용. 위 값을 num 빈 리스트에 넣기 위해 list로 변경

  for i in per:
    if is_prime_number(i) == True:
      answer += 1
  return answer

'''
에라토스테네스의 체로 풀고 싶었으나 포기..
'''