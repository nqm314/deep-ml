def calculate_brightness(img):
	# Write your code here
  n = len(img)

  if n <= 0:
    return -1
  
  m = len(img[0])

  sum = 0

  for i in range(n):
    if len(img[i]) != m:
      return -1
    
    for j in range(m):
      if img[i][j] < 0 or img[i][j] > 255:
        return -1

      sum += img[i][j]

  return sum / (n*m)