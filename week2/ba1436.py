# 영화감독 숌

n = int(input())
defalt = 666
count = 0

while True:
  if '666' in str(defalt):
    count += 1
  if n == count:
    print(defalt)
    break
  defalt += 1

'''
n = int(input())
defalt = 665
count = 0

while True:
  defalt += 1 #defalt값을 앞에 둘 경우에는 defalt값을 666이 아닌 665로 해야 한다.
  if '666' in str(defalt):
    count += 1
  if n == count:
    print(defalt)
    break
'''