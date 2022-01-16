# 프로그래머스 - 정렬 - 가장 큰 수

def solution(numbers):
  li =[]
  for i in numbers: #문자열로 변경하여 새로운 리스트에 넣음
    li.append(str(i))
  
  li.sort(key= lambda a: a*3) #리스트 안에 있는 각 문자열을 *3을 함 
  # ex) 3 -> 333 31->313131 이렇게 되면 비교할 때 3이 더 크게 정렬함
  li.reverse() # 정렬한 것을 내림차순으로

  answer = ''.join(li) #정렬한 리스트안의 문자열들을 하나로 합쳐주기
  if int(answer) == 0: #만약 안에 들어있는 수가 0으로만 이루어져 있다면 0하나로 출력
    answer = '0'
    # ex) [0,0,0,0] ->결과 0000이 아닌 0으로 출력하도록 함
  return answer
  
  # 조금 더 확실하게 하는 방법
  # if answer.count("0") == len(answer): 
  #   answer = "0"


print(solution([1,0,0,0]))



'''
def solution(numbers):
  li =[]
  for i in numbers:
    li.append(str(i))
  
  # for i in range(len(numbers)-1):
  #   for j in range(len(numbers)):
  #     if (int(li[i][0]) == int(li[j][0])) and (len(li[i]) < len(li[j])):
  #       li[i] = li[i] + li[i][0] * ((len(li[j]) - len(li[i])))
  # li.sort(key= lambda a: a[0])
  li.sort(key= lambda a: (a[0], hi(a)))
  li.reverse()
  print(li)
  answer = ''.join(li)
  # answer = ''
  return answer

def hi(a):
  for i in range(len(a)-1):
      for j in range(len(a)):
        if (int(a[i][0]) == int(a[j][0])) and (len(a[i]) < len(a[j])):
          a[i] = a[i] + a[i][0] * ((len(a[j]) - len(a[i])))
          print(a[i])

print(solution([3,30,34,5,9]))
'''