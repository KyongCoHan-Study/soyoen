# 덩치

n = int(input())
x = [] #몸무게
y = [] #키
rank = [] #순위

for i in range(n):
  w, h = map(int,input().split())
  x.append(w)
  y.append(h)
  rank.append(1)

for i in range(n):
  for j in range(n):
    if (x[i] > x[j]) and (y[i] > y[j]):
      rank[j] += 1

# rank는 정수이기 때문에 map을 사용하여 문자열(str)로 변환하게 바꾸기
result = ' '.join(map(str,rank))
print(result)

'''
join함수
--- '구분자'.join(리스트)
'구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줍니다.
'_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로 문자열을 만들어서 반환해 줍니다.

'''