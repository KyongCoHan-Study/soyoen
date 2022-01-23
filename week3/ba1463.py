# 1로 만들기

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1) #계산된 횟수 저장
# n+1인 이유는 첫번째 수는 dp[2]이기 때문 (최소 한번은 돌아가니까(n이1 제외) 2부터 시작)

for i in range(2,n+1):
  dp[i] = dp[i-1] + 1 # 1을 빼준다 
  # 이전 횟수에 +1 카운팅 (1 빼기)

  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i//2]+1) #1을 더하는 이유, dp는 계산한 횟수를 저장하는 것이기 때문에
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i//3]+1) #dp[i]에 더하지 않는 이유, 1을 뺄 때 1을 더해준 이력이 있어서

print(dp[n])

# 이해 안된다면 종이에 직접 대입해서 해보기
'''
import sys
read = sys.stdin.readline

N = int(read())
cache = {1: 0, 2: 1}

def dp(n):
    if n in cache:
        return cache[n]
	
    # 핵심 코드
    cnt = 1 + min(dp(n//3) + n%3, dp(n//2) + n%2)
    cache[n] = cnt
    return cnt
    
print(dp(N))
'''