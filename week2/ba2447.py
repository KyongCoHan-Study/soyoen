# 별 찍기 - 10
# 별을 찍을 때 한줄씩 찍었음

def write_star(n):
  li = [] # 별을 담을 리스트
  for i in range(3*len(n)):
    if i // len(n) == 1: #n이 3으로 나누어 떨어지지 않는다면, 가운데 공백 (n의 길이만큼)
      li.append(n[i % len(n)] + ' ' * len(n) + n[i % len(n)])
    else: #n이 3으로 나누어 떨어진다면, 공백없이 가득 채우기
      li.append(n[i % len(n)] * 3)
  return li

star = ['***','* *','***']
n = int(input())
count = 0 #반복횟수

while n != 3:
  n = int(n/3)
  count += 1

for i in range(count):
  star = write_star(star)

for i in star:
  print(i)

# for i in range(1,n//3):
#   if 3**i == n:
#     count = i
# print(count)

'''
def star(n: int, x: list) -> list:
  out = []
  if n == 3:
    return x
  else:
    for i in x: #위에 처음 3개 구역
      out.append(i*3)
    for i in x: #가운데 3개 구역 (중앙 비어있음)
      out.append(i+' '*len(x)+i)
    for i in x: #마지막 3개 구역
      out.append(i*3)
    return star(n//3, out)

if __name__ == '__main__':
  n = int(input())
  first = ['***','* *','***']
  final = star(n,first)
  for i in final:
    print(i)
'''