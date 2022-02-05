# LCS

a = input()
b = input()
a_len = len(a)
b_len = len(b)

LCS = [[0]*(a_len+1) for i in range(b_len+1)]

for i in range(1, a_len + 1):
  for j in range(1, b_len + 1):
    if a[i - 1] == b[j - 1]:
      LCS[i][j] = LCS[i - 1][j - 1] + 1
    else:
      LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(LCS[-1][-1])


# 최장공통부분수열 및 최장공통부분문자열 설명글
# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence