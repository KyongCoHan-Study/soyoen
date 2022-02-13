# 랜선 자르기
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = []

def find(nums, n):
  start = 1
  end = max(nums)
  mid = (start + end) / 2

  while start <= end:
    len_count = sum([nums[i] // mid for i in range(len(nums))])
    if len_count >= n: # n보다 같거나 커야 함
      start = mid + 1 # 랜선의 길이가 최대가 되어야 하므로 mid값을 올림
    else: # n보다 크게 만들기 위해 mid 값을 내림
      end = mid - 1
    mid = (start + end) // 2 # 위의 조건에 맞추어 mid 재설정
  return round(mid)

for i in range(k):
  lan.append(int(input()))
print(find(lan, n))
