# 프로그래머스 - 힙 - 더 맵게

import heapq

def solution(scoville, k):
  answer = 0
  heapq.heapify(scoville)

  while scoville[0] < k:
    mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
    heapq.heappush(scoville, mix)
    answer += 1
    
    if len(scoville) == 1 and scoville[0] < k:
      return -1
  return answer