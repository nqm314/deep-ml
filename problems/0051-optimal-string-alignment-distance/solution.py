import numpy as np

def OSA(source: str, target: str) -> int:
  # Your code here
  dp = np.array([[0 for _ in range(len(target)+1)] for _ in range(len(source)+1)])
  # print(dp)

  for i in range(1,len(source)+1):
    dp[i][0] = i

  for i in range(1,len(target)+1):
    dp[0][i] = i

  for i in range(1, len(source)+1):
    for j in range(1, len(target)+1):
    #   print(dp)
      if source[i - 1] == target[j - 1]:
        dp[i][j] = dp[i - 1][j - 1]
      else:
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

      if i > 1 and j > 1 and source[i - 1] == target[j-2] and source[i-2] == target[j - 1]:
        dp[i,j] = min(dp[i,j], dp[i-2, j-2] + 1)

#   print(dp)
  return dp[- 1][- 1]