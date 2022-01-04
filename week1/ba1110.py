# 더하기 사이클

n = input()
count = 0

if int(n) < 10:
  n = '0' + n

result = n

while (n != result) or (count==0):
  result = result[-1] + str(int(result[0])+int(result[1]))[-1]
  count += 1
print(count)

# 0을 입력했을 때 하나라도 카운트를 해주기 위해서 count==0을 넣어야 함
# 해당 숫자 문자열의 마지막 수를 뽑기 위해서 [-1]로 할 것
# 돌아오기 전에 두자리 수를 넘는 경우가 있기 때문임! [1]로 하면 오류 남