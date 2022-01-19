#피보나치 함수

t = int(input())
for i in range(t):
  n = int(input())
  zero = [1,0,1]
  one = [0,1,1]
  if n >= 3:
    for i in range(3,n+1): # 0과1이 3번째부터 피보나치처럼 나오기 때문에 3부터 시작
      zero.append(zero[i-1]+zero[i-2]) # 0의 피보나치
      one.append(one[i-1]+one[i-2]) # 1의 피보나치
  print(zero[n], one[n])

'''
       0  1  2  3  4  5  6  7 
0 출력 1  0  1  1  2  3  5  8
1출력  0  1  1  2  3  5  8  13

0이 출력된 횟수를 보면 4번째부터 피보나치 수열처럼 나옴
1은 3번째부터 나온다
그래서 0과 1이 출력되는 횟수를 각각 피보나치 수열을 이용하여 나타낸 것임.
'''