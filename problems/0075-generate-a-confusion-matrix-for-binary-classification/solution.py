from collections import Counter

def confusion_matrix(data):
	# Implement the function here
  TP, FN, FP, TN = 0,0,0,0
  for dt in data:
    TP += dt[0] == 1 and dt[0] == dt[1]
    FN += dt[0] == 1 and dt[0] != dt[1]
    FP += dt[0] == 0 and dt[0] != dt[1]
    TN += dt[0] == 0 and dt[0] == dt[1] 

  return [[TP, FN], [FP, TN]]